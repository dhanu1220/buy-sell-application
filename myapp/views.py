from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Product, OrderDetail
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http.response import HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
import stripe
def index(request):
    return HttpResponse("hello")

# *** FUNCTION BASED VIEW TO PRINT LIST OF PRODUCTS ***

# def products(request):
#     products = Product.objects.all()
#     context={
#         'products':products
#     }
#     return render(request,'myapp/index.html',context)

class ProductListView(ListView):
    model = Product
    template_name = 'myapp/index.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Product.objects.filter(name__icontains=query)
        return Product.objects.all()

# *** FUNCTION BASED VIEW FOR DETAILS PAGE ***

# def product_detail(request,id):
#     product = Product.objects.get(id=id)
#     context={
#         'product':product
#     }
#     return render(request,'myapp/product_detail.html',context)

class ProductDetailView(DetailView):
    model = Product
    template_name='myapp/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg='pk'

    def get_context_data(self, **kwargs):
        context= super(ProductDetailView,self).get_context_data(**kwargs)
        context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

# @login_required
# def add_product(request):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         price=request.POST.get('price')
#         desc=request.POST.get('desc')
#         seller_name=request.user
#         image=request.FILES['upload']
#         product=Product(name=name,price=price,desc=desc,image=image,seller_name=seller_name)
#         product.save()
#     return render(request, 'myapp/addproduct.html')

class ProductCreateView(CreateView):
    model = Product
    fields = ['name','price','desc','image','seller_name']

# def update_product(request,id):
#     product = Product.objects.get(id=id)
#     if request.method=='POST':
#         product.name=request.POST.get('name')
#         product.price=request.POST.get('price')
#         product.desc=request.POST.get('desc')
#         product.image=request.FILES['upload']
#         product.save()
#         return redirect('/myapp/products')
#     context={
#         'product':product
#     }
#     return render(request,'myapp/updateproduct.html',context)

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name','price','desc','image','seller_name']
    template_name_suffix = '_update_form'

# def delete(request,id):
#     product = Product.objects.get(id=id)
#     context={
#         'product':product
#     }
#     if request.method=='POST':
#         product.delete()
#         return redirect('/myapp/products')
#     return render(request,'myapp/delete.html',context)

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('myapp:products')

def my_listings(request):
    products = Product.objects.filter(seller_name = request.user)
    context={
        'products': products,
    }
    return render(request,'myapp/mylistings.html',context)

@csrf_exempt
def create_checkout_session(request, id):
    product = get_object_or_404(Product,pk=id)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        customer_email= request.user.email,
        payment_method_types=['card'],
        line_items=[
            {
                'price_data':{
                    'currency':'usd',
                    'product_data':{
                        'name':product.name,
                    },
                    'unit_amount':int(product.price*100),
                },
                'quantity':1,
            }
        ],
        mode ='payment',
        success_url = request.build_absolute_uri(reverse('myapp:success'))+"?session_id={CHECKOUT_SESSION_ID}",
        cancel_url = request.build_absolute_uri(reverse('myapp:failed')),

    )
    order = OrderDetail()
    order.customer_username = request.user.customer_username
    order.product = product
    order.stripe_payment_intent = checkout_session['payment_intent']
    order.amount = int(product.price*100)
    order.save()
    return JsonResponse({'sessionId':checkout_session.id})
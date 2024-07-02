from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView
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

def delete(request,id):
    product = Product.objects.get(id=id)
    context={
        'product':product
    }
    if request.method=='POST':
        product.delete()
        return redirect('/myapp/products')
    return render(request,'myapp/delete.html',context)

def my_listings(request):
    products = Product.objects.filter(seller_name = request.user)
    context={
        'products': products,
    }
    return render(request,'myapp/mylistings.html',context)
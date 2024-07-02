from django.shortcuts import render
from django.shortcuts import redirect
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp/products')
    form = NewUserForm()
    context={
        'form': form,
    }
    return render(request,'users/register.html',context)

@login_required
def profile(request):
    return render(request,'users/profile.html')

def create_profile(request):
    if request.method=='POST':
        contact_number=request.POST.get('contact_number')
        image=request.FILES['upload']
        user=request.user
        profile=Profile(user=user,image=image,contact_number=contact_number)
        profile.save()
    return render(request,'users/createprofile.html')

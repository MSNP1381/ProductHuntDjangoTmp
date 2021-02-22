from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product


# Create your views here.
def home(request):
    return render(request, 'home.html')


@login_required
def create_product(request):
    if request.method == 'POST':
        prod = Product()
        prod.title = request.POST['title']
        prod.body = request.POST['body']
        prod.url = request.POST['url']
        prod.image = request.FILES['image']
        prod.icon = request.FILES['icon']
        prod.hunter=request.user
        prod.save()
        return redirect('home')
        # return render(request,'home.html',{'message':"""dear hunter
        # your Product is saved successfully &#128525"""})
    else:
        return render(request, 'producthunt/createProduct.html')


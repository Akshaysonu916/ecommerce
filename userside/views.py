from django.shortcuts import render,redirect
from .forms import Product_form
from . models import Products,User
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError

# Create your views here.

@login_required(login_url='signin')
def add_products(request):
    print('add products working')
    form = Product_form()
    if request.method =="POST":
        form = Product_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addproducts')
        else:
            form=Product_form()
    context = {
        "form":form
    }
    return render(request,"addproducts.html",context)

def signup_view(request):
    if request.method == 'POST':
        print('working signup')
        errors={}
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        print('email',email)
        print('username',username)
        print('password',password)
        print('confirm password',confirm_password)

        if password!=confirm_password:
            errors["confirm_password"]="Password do not match!"
        print('password validation completerd')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'username is already taken')
            print('email already taken')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken')
            print('email already taken')
            
        if errors:
            return render(request,'signup.html',{'errors':errors})

        User.objects.create_user(
        email=email,
        username=username,
        password=password,   
        )
        print('created')
        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('signin')
    return render(request,'signup.html')

def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('products')
            else:
                return redirect('home')


        else:
            messages.error(request, 'Invalid username or password')
            return redirect('signin')
    return render(request,'signin.html')


def logout_view(request):
    logout(request)
    return redirect('signin')

def home_view(request):

    return render(request,'home.html',{'user':request.user})

def product_view(request):
    pdt=Products.objects.all()
    return render(request,'products.html',{'products':pdt})

def user_product_view(request):
    try:
        searching = request.GET.get('searching', '')
        if searching:
            pdt = Products.objects.filter(product_name__icontains=searching)
        else:
            pdt = Products.objects.all()
        return render(request, 'userproducts.html', {'products': pdt})
    except Products.DoesNotExist:
        pdt = Products.objects.none()


def edit_product(request,id):
    product = Products.objects.get(id=id)
    if request.method == "POST":
        form = Product_form(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = Product_form(instance=product)
    return render(request, 'editproducts.html', {'form': form, 'product': product})

def delete_product(request, id):
    product = Products.objects.get(id=id)
    product.delete()
    return redirect('products') 

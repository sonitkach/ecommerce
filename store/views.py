from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm  
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder

def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    

    products=Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)

def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print ('productId:', productId)
    print ('action:', action)
    customer=request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action=='add':
        orderItem.quantity = (orderItem.quantity+1)
    elif action=='remove':
         orderItem.quantity = (orderItem.quantity-1)
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse('item was added', safe=False) 


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data=json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    
    
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    if order.shipping == True:
        Address.objects.create(
            customer=customer,
			    order=order,
			    address=data['shipping']['address'],
			    city=data['shipping']['city'],
			    state=data['shipping']['state'],
			    zipcode=data['shipping']['zipcode'],
			)
			    

    return JsonResponse('payment submitted', safe=False)

def signUpView(request):
    
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            user_group = Group.objects.get(name='User')
            user_group.user_set.add(signup_user)
    else:
        form = SignUpForm()
    
    data = cartData(request)
    cartItems = data['cartItems'] 
    context = {'cartItems':cartItems, 'form': form}

    return render(request, 'store/signup.html', context)



def loginView(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username=request.POST['username']
                password=request.POST['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    
                    return redirect ('store')
                else:
                    return redirect ('signup')
        else:
            form = AuthenticationForm()

        data = cartData(request)
        cartItems = data['cartItems'] 
        context = {'cartItems':cartItems, 'form': form}
        
        return render (request, 'store/login.html', context)

def signoutView(request):
    logout(request)
    return redirect('login')


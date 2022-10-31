import decimal
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from pycoingecko import CoinGeckoAPI
from accounts.models import Transaction


def user_login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.info(request, 'Disabled Account')
            else:
                messages.info(request, 'Wrong Username or Password')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)

    return redirect('index')


def user_register(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')


def add_crypto(request):
    user_id = request.user.id
    coin_id = request.POST['coin_id']
    quantity = request.POST['quantity']
    price = request.POST['price']
    amount = int(quantity) * decimal.Decimal(price)
    user = User.objects.get(id=user_id)

    transaction = Transaction(coin_id=coin_id, amount=amount, quantity=quantity, price=price)
    transaction.save()
    transaction.user.add(user)

    return redirect('dashboard')

from itertools import product

from allauth.account.views import email
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from social.pipeline import user


from .models import *


def store(request):
    products = Product.objects.all()
    context = {'products': products}
    # context = {}

    return render(request, 'store.html', context)


def buy(request):
    if request.method == 'POST':
        try:
            send_mail_after_buy()
            return redirect('success_buy.html')

        except Exception as e:
            print(e)

    return render(request, 'store.html')


def product_detail(request, pk):
    products = Product.objects.get(id=pk)
    context = {'products': products}
    return render(request, "product_detail.html", context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items': items}

    return render(request, 'buy.html', context)


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)


def customer(request):
    context = {}
    return render(request, 'user_profile.html', context)


def send_mail_after_buy():
    subject = 'Buy Products'
    message = f'Hi paste the link to verify your account'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['sandra@techversantinfo.com']
    send_mail(subject, message, email_from, recipient_list)

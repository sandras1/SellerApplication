from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect


@login_required
# Create your views here.
def home_page(request):
    return render(request, 'index_old.html')



from django.urls import path
from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('customer/', views.customer, name="customer"),
    path('product_detail/<int:pk>', views.product_detail, name='product_detail'),
    path('buy/', views.buy, name="buy"),

]

from django.urls import path
from . import views

app_name = "carts"


urlpatterns = [
    path('carts/add/<int:id>/', views.cart_add, name='cart_add'),
    path('carts/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('carts/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('carts/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('carts/cart_clear/', views.cart_clear, name='cart_clear'),
    path('carts/cart-detail/',views.cart_detail,name='cart_detail'),
]
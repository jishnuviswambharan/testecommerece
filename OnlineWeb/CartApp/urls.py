from django.urls import path
from . import views

app_name = 'CartApp'

urlpatterns = [

    path('cart', views.cartdetail, name='cartdetail'),
    path('add/<int:product_id>/', views.add_cart, name="add_cart"),    
    path('delete/<int:product_id>/', views.cart_delete, name = 'cart_delete'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('address',views.delivery, name='delivery')
]
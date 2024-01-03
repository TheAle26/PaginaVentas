from django.urls import path
from AppVentas import views

urlpatterns=[
    path('inicio',views.inicio),
    path('catalogo',views.product_list),
    path('carrito',views.cart_detail),
    path('mi_usuario',views.mi_usuario),

]
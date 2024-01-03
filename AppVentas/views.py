from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .models import Cart, CartItem
#from django.forms import CartAddProductForm
# Create your views here.

def inicio(request):
    return render(request,"AppVentas/inicio.html")


def mi_usuario(request):
    return render(request,"AppVentas/usuario.html")

#def ventas(request):
    return render(request,"AppVentas/ventas.html")


#aca para que se vean los productos
def product_list(request):
    products = Product.objects.all()
    return render(request, 'AppVentas/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'AppVentas/product_detail.html', {'product': product})

# Otras vistas (carrito, checkout, perfil de usuario, historial de pedidos) deberán ser implementadas según las necesidades específicas de tu aplicación.
#ahora para el carrito


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'AppVentas/cart_detail.html', {'cart': cart})

def cart_add(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

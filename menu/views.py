from django.shortcuts import get_object_or_404, render

from cart.cart import Cart
from shop.models import Product, Suveniru, Specials, Contact


def product_list(request, category_slug=None):
    cart = Cart(request)
    products = Product.objects.filter(available=True)
    return render(request, 'form.html', {'products': products, 'cart': cart})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request,
                  'product_detail.html',
                  {'product': product}
                  )

def suveniru_list(request, category_slug=None):
    cart = Cart(request)
    suvenirus = Suveniru.objects.filter(available=True)
    return render(request, 'suveniru.html', {'suvenirus': suvenirus, 'cart': cart})


def suveniru_detail(request, id, slug):
    suveniru = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request,
                  'suveniru_detail.html',
                  {'suveniru': suveniru}
                  )

def main(request):
    return render(request, 'main.html')

def specials_list(request, category_slug=None):
    cart = Cart(request)
    specialss = Specials.objects.filter(available=True)
    return render(request, 'specials.html', {'specialss': specialss, 'cart': cart})


def specials_detail(request, id, slug):
    specials = get_object_or_404(Specials, id=id, slug=slug, available=True)
    return render(request,
                  'specials-detail.html',
                  {'specials': specials}
                  )

def contact_list(request, category_slug=None):
    contacts = Contact.objects.filter(available=True)
    return render(request, 'contact.html', {'contacts': contacts})


def contact_detail(request, id, slug):
    contact = get_object_or_404(Specials, id=id, slug=slug, available=True)
    return render(request,
                  'contact-detail.html',
                  {'contact': contact}
                  )



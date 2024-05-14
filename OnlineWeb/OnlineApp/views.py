from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator, InvalidPage, EmptyPage


# Create your views here.
# def allProdCat( request, c_slug = None):
#     c_page = None
#     products = None
#     if c_slug != None:

#         c_page = get_object_or_404(Category, slug = c_slug)

#         products = Product.objects.all().filter(category=c_page, available = True)

#     else:
#         products = Product.objects.all().filter(available = True)
        
#     return render(request, 'category.html', {'category': c_page, 'products': products})


def allProdCat(request, c_slug=None):
    c_page=None
    product_list = None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        product_list=Product.objects.all().filter(category=c_page, available = True)
    else:
        product_list=Product.objects.all().filter(available = True)
    paginator = Paginator(product_list,4)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (InvalidPage, EmptyPage):
        products=paginator.page(paginator.num_pages)
    return render (request, 'category.html', {'category':c_page, 'products': products})


def productdetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug = c_slug, slug = product_slug)

    except Exception as e:
        raise e 
    return render (request, 'productdeatil.html', {'product': product})



#video section sample

def exclusive(request):
    return render(request, 'exclusive.html')
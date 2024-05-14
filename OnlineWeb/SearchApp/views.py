from django.shortcuts import render
from OnlineApp.models import Product
from . import views
from django.db.models import Q

# Create your views here.
def searchresults(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains = query) | Q(description__contains = query))
    return render (request, 'search.html', {'query': query, 'products': products})
 
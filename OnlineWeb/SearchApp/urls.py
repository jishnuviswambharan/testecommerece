from django.urls import path
from .import views

app_name = 'SearchApp'

urlpatterns =[
    path('search', views.searchresults, name='sreachresults')
]
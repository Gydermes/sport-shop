from django.urls import path

from . import views
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', main),

    path('form/', views.product_list, name='product_list'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('suveniru/', views.suveniru_list, name='suveniru_list'),
    path('<int:id>/<slug:slug>/', views.suveniru_list, name='suveniru_detail'),
    path('specials/', views.specials_list, name='specials_list'),
    path('<int:id>/<slug:slug>/', views.specials_detail, name='specials_detail'),
    path('contact/', views.contact_list, name='contact_list'),
    path('<int:id>/<slug:slug>/', views.contact_detail, name='contact_detail'),

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='product_list'),
    path('', views.list, name='product_list_by_category'),
    path('', views.detail, name='product_detail'),
]
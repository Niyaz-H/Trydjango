from django.contrib import admin
from django.urls import include, path

from products.views import dynamic_lookup_view, product_detail_view, product_delete_view, product_list_view

app_name='products'
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
]

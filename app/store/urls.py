from django.urls import path
from . import views

urlpatterns = [
    path('manufacturers/', views.manufacturer_add, name='manufacturer_add'),
    path('manufacturers/<int:contract_id>/', views.store_views, name='get_manufacturers_by_contract_id'),
    path('orders/', views.order_add, name='order_add'),
    path('products/', views.product_add, name='product_add'),
    path('contracts/', views.contract_add, name='contract_add'),
]
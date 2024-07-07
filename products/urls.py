from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path(
        'delete/<int:product_id>/', views.delete_product, name='delete_product'
        ),
    path(
        'product/<int:product_id>/add-to-favorites/',
        views.add_to_favorites, name='add_to_favorites'),
    path(
        'favorites/<int:product_id>/remove/',
        views.remove_from_favorites, name='remove_from_favorites'),
    path('favorites/', views.favorite_list, name='favorite_list'),
]

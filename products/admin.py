from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Product, Category, Review


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'rating',
        'image1',
        'image2',
        'image3',
    )
    search_fields = ['sku', 'name', 'description', ]
    ordering = ('sku',)
    summernote_fields = ('description',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'created_at']
    list_filter = ['product', 'rating', 'created_at']
    search_fields = ['user__username', 'product__name', 'comment']


admin.site.register(Category, CategoryAdmin)

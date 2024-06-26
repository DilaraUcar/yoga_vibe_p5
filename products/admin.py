from django.contrib import admin
from .models import Product, Category
from django_summernote.admin import SummernoteModelAdmin

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
    search_fields = ['sku', 'name', 'description',] 
    ordering = ('sku',)
    summernote_fields = ('description',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Category, CategoryAdmin)
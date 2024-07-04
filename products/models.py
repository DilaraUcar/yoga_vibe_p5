from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Represents a category for grouping products.
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Represents a product available for sale.
    """

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=10)
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    image1 = models.ImageField(upload_to='product_imgs/', default='product_imgs/noimage.png', null=True, blank=True)
    image2 = models.ImageField(upload_to='product_imgs/', null=True, blank=True)
    image3 = models.ImageField(upload_to='product_imgs/', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Check if any of the image fields are empty
        if not self.image1 and not self.image2 and not self.image3:
            self.image1 = 'product_imgs/noimage.png'

        super().save(*args, **kwargs)


class ProductRecommendation(models.Model):
    product = models.ForeignKey(Product, related_name='main_product', on_delete=models.CASCADE)
    recommended_product = models.ForeignKey(Product, related_name='recommended_product', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name} recommends {self.recommended_product.name}'


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')
        verbose_name_plural = 'Favorites'

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'



class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    title = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.product.name}'
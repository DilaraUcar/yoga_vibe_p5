from django.db import models

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
    image1 = models.ImageField(upload_to='product_imgs/', default='product_imgs/noimage.png', null=True, blank=True)
    image2 = models.ImageField(upload_to='product_imgs/', null=True, blank=True)
    image3 = models.ImageField(upload_to='product_imgs/', null=True, blank=True)
    # Add more image fields as needed...

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Check if any of the image fields are empty
        if not self.image1 and not self.image2 and not self.image3:
            self.image1 = 'product_imgs/noimage.png'

        super().save(*args, **kwargs)

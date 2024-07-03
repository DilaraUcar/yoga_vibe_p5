from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def star_rating(rating):
    full_stars = int(rating)
    half_stars = round(rating - full_stars)
    empty_stars = 5 - full_stars - half_stars
    
    stars = '<i class="fa-solid fa-star"></i>' * full_stars
    stars += '<i class="fas fa-star-half-alt"></i>' * half_stars
    stars += '<i class="fa-regular fa-star"></i>' * empty_stars
    
    return mark_safe(stars)

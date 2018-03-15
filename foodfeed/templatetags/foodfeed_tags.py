from django import template
from foodfeed.models import *

register = template.Library()


@register.assignment_tag
def get_pic_details(picture):
    ratings = Rating.objects.filter(picture=picture)

    health_sum = 0
    style_sum = 0
    cooking_sum = 0

    for rating in ratings:
        health_sum += rating.health_rating
        style_sum += rating.style_rating
        cooking_sum += rating.cooking_rating

    return [health_sum//len(ratings),
            style_sum//len(ratings),
            cooking_sum//len(ratings)]

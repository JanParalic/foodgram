from django import template
from foodfeed.models import *

register = template.Library()


@register.assignment_tag
def get_pic_ratings(picture):
    ratings = Rating.objects.filter(picture=picture)

    health_sum = 0
    style_sum = 0
    cooking_sum = 0

    if len(ratings) == 0:
        return {"health": 0,
                "style": 0,
                "cooking": 0}

    for rating in ratings:
        health_sum += rating.health_rating
        style_sum += rating.style_rating
        cooking_sum += rating.cooking_rating

    return {"health": health_sum//len(ratings),
            "style": style_sum//len(ratings),
            "cooking": cooking_sum//len(ratings)}


@register.assignment_tag
def get_user_stats(user):
    pictures = Picture.objects.filter(author=user)

    health_sum = 0
    style_sum = 0
    cooking_sum = 0

    if len(pictures) == 0:
        return {"health": 0,
                "style": 0,
                "cooking": 0}

    for picture in pictures:
        pic_stats = get_pic_ratings(picture)
        health_sum += pic_stats[0]
        style_sum += pic_stats[1]
        cooking_sum += pic_stats[2]

    return {"health": health_sum//len(pictures),
            "style": style_sum//len(pictures),
            "cooking": cooking_sum//len(pictures)}


@register.assignment_tag
def get_position(picture, feed):
    counter = 0

    for pic in feed:
        if pic == picture:
            return counter
        counter += 1

    return -1

from django import template
from foodfeed.models import *

import datetime
from django.utils import timezone

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
        health_sum += pic_stats["health"]
        style_sum += pic_stats["style"]
        cooking_sum += pic_stats["cooking"]

    return {"health": health_sum//len(pictures),
            "style": style_sum//len(pictures),
            "cooking": cooking_sum//len(pictures)}


@register.assignment_tag
def get_user_uploads(user):
    return Picture.objects.filter(author=user).order_by("-date_published")


@register.assignment_tag
def get_picture_comments(picture):
    return Comment.objects.filter(picture=picture).order_by("date_published")


@register.assignment_tag
def get_date_posted(picture):
    posted = picture.date_published
    now = timezone.now()

    difference = now - posted

    if difference > datetime.timedelta(days=2):
        return str(difference.days) + " days ago"
    elif difference > datetime.timedelta(days=1):
        return "Yesterday at %s%s" % (difference.seconds // 3600, difference.seconds // 60)
    elif difference > datetime.timedelta(seconds=3600):
        return "%s hours ago" % (difference.seconds // 3600)
    else:
        return "%s minutes ago" % (difference.seconds // 60)


@register.assignment_tag
def get_position(picture, feed):
    counter = 0

    for pic in feed:
        if pic == picture:
            return counter
        counter += 1

    return -1

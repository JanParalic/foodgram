import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'foodgram.settings')

import django
django.setup()

from foodfeed.models import User, Picture, Rating, Comment


def populate():
    users = [
        {"email": "1234567j@student.gla.ac.uk", "first_name": "Matthew",
         "last_name": "Jones", "date_joined": "2017-08-12", "is_active": True,
         "is_staff": "False", "avatar": "profile1.jpg"},

        {"email": "7382645l@student.gla.ac.uk", "first_name": "Laura",
         "last_name": "Lawrence", "date_joined": "2017-10-03", "is_active": True,
         "is_staff": "False", "avatar": "profile2.jpg"},

        {"email": "7362514s@student.gla.ac.uk", "first_name": "Sarah",
         "last_name": "Smith", "date_joined": "2018-02-18", "is_active": True,
         "is_staff": "True", "avatar": "profile3.jpg"},
    ]

    pictures = [
        {"author": "1234567j@student.gla.ac.uk",
         "description": "Made this delicious apple pie for my flatmate's birthday!",
         "date_published": "2018-03-09 14:07:19", "picture": "apple_pie.jpg"},

        {"author": "7362514s@student.gla.ac.uk",
         "description": "I tried this recipe for protein pancakes: one egg, one banana, 1/2 cup of oats.",
         "date_published": "2018-02-10 11:20:45", "picture": "pancakes.jpg"},
    ]

    reviews = [
        {"author": "7382645l@student.gla.ac.uk", "picture": "2018-03-09 14:07:19", "rating": [2,3,4]},
        {"author": "7362514s@student.gla.ac.uk", "picture": "2018-03-09 14:07:19", "rating": [4,5,1]},
        {"author": "1234567j@student.gla.ac.uk", "picture": "2018-02-10 11:20:45", "rating": [3,4,5]},
        {"author": "7382645l@student.gla.ac.uk", "picture": "2018-02-10 11:20:45", "rating": [5,1,2]},
    ]

    comments = [
        {"author": "7382645l@student.gla.ac.uk", "picture": "2018-03-09 14:07:19", "comment": "Looks delicious"},
        {"author": "1234567j@student.gla.ac.uk", "picture": "2018-02-10 11:20:45",
         "comment": "Can I have the recipe please =)"},
        {"author": "7382645l@student.gla.ac.uk", "picture": "2018-02-10 11:20:45",
         "comment": "I made some just yesterday as well"},
    ]

    for user in users:
        author = add_user(user["email"], user["first_name"], user["last_name"], user["date_joined"],
                 user["is_active"], user["is_staff"], user["avatar"])

        for pic in pictures:
            if user["email"] == pic["author"]:
                add_picture(author, pic["picture"], pic["description"], pic["date_published"])

    for picture in pictures:
        for review in reviews:
            if review["picture"] == picture["date_published"]:
                add_review(User.objects.get(email=review["author"]),
                           Picture.objects.get(date_published=picture["date_published"]),
                           review["rating"])

        for comment in comments:
            if comment["picture"] == picture["date_published"]:
                add_comment(User.objects.get(email=comment["author"]),
                            Picture.objects.get(date_published=picture["date_published"]),
                            comment["comment"])


def add_user(email, first_name, last_name, date_joined, is_active, is_staff, avatar):
    u = User.objects.get_or_create(email=email)[0]
    u.first_name = first_name
    u.last_name = last_name
    u.date_joined = date_joined
    u.is_active = is_active
    u.is_staff = is_staff
    u.avatar = avatar
    u.save()
    return u


def add_picture(author, picture, description, date_published):
    p = Picture.objects.get_or_create(author=author, picture=picture)[0]
    p.description = description
    p.date_published = date_published
    p.save()
    return p


def add_review(author, picture, rating):
    review = Rating.objects.get_or_create(author=author, picture=picture)[0]
    review.health_rating = rating[0]
    review.style_rating = rating[1]
    review.cooking_rating = rating[2]
    review.save()
    return review


def add_comment(author, picture, comment):
    com = Comment.objects.get_or_create(author=author, picture=picture)[0]
    com.comment = comment
    com.save()
    return com


if __name__ == '__main__':
     print("Starting Foodgram population script...")
     populate()
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'foodgram.settings')

import django
django.setup()

from foodfeed.models import User, Picture


def populate():
    users = [
        {"email": "1234567j@student.gla.ac.uk", "first_name": "Matthew",
         "last_name": "Jones", "date_joined": "12/08/17", "is_active": True,
         "is_staff": "False", "avatar": "media/profile1.jpg"},

        {"email": "7382645l@student.gla.ac.uk", "first_name": "Laura",
         "last_name": "Lawrence", "date_joined": "10/03/17", "is_active": True,
         "is_staff": "False", "avatar": "media/profile2.jpg"},

        {"email": "7362514s@student.gla.ac.uk", "first_name": "Sarah",
         "last_name": "Smith", "date_joined": "18/02/18", "is_active": True,
         "is_staff": "True", "avatar": "media/profile3.jpg"}
    ]

    pictures = [
        {"author": "1234567j@student.gla.ac.uk",
         "description": "Made this delicious apple pie for my flatmate's birthday!",
         "date_published": "22/01/18", "picture": "media/apple_pie.jpg"},

        {"author": "7362514s@student.gla.ac.uk",
         "description": "I tried this recipe for protein pancakes: one egg, one banana, 1/2 cup of oats.",
         "date_published": "19/02/18", "picture": "media/pancakes.jpg"}
    ]

    for user in users:
        add_user(user["email"], user["first_name"], user["last_name"], user["date_joined"],
                 user["is_active"], user["is_staff"], user["avatar"])

    for pic in pictures:
        add_picture(pic["author"], pic["picture"], pic["description"], pic["date_published"])


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
    p = Picture.objects.get_or_create(author=author, picture=picture)
    p.description = description
    p.date_published = date_published
    p.save()
    return p


if __name__ == '__main__':
     print("Starting Foodgram population script...")
     populate()

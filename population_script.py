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
         "is_staff": False, "avatar": "profile1.jpg", "password": "qwerty"},

        {"email": "7382645l@student.gla.ac.uk", "first_name": "Laura",
         "last_name": "Lawrence", "date_joined": "2017-10-03", "is_active": True,
         "is_staff": False, "avatar": "profile2.jpg", "password": "comic"},

        {"email": "7362514s@student.gla.ac.uk", "first_name": "Sarah",
         "last_name": "Smith", "date_joined": "2018-02-18", "is_active": True,
         "is_staff": False, "avatar": "profile3.jpg", "password": "oaktree"},

        {"email": "8382773l@student.gla.ac.uk", "first_name": "Amy",
         "Lane": "Smith", "date_joined": "2018-01-15", "is_active": True,
         "is_staff": False, "avatar": "profile4.jpg", "password": "teapot"},

        {"email": "2283116s@student.gla.ac.uk", "first_name": "Jacob",
         "last_name": "Stafford", "date_joined": "2018-01-22", "is_active": True,
         "is_staff": False, "avatar": "profile5.jpg", "password": "strangers"},

        {"email": "tom_swindon87@fakemail.com", "first_name": "Tom",
         "last_name": "Swindon", "date_joined": "2018-03-10", "is_active": True,
         "is_staff": False, "avatar": "profile6.jpg", "password": "ridiculous"},

        {"email": "jessica09law@fakemail.com", "first_name": "Jessica",
         "last_name": "Law", "date_joined": "2018-02-19", "is_active": True,
         "is_staff": False, "avatar": "profile7.jpg", "password": "saturdays"}
    ]

    pictures = [
        {"author": "1234567j@student.gla.ac.uk",
         "description": "Made this delicious apple pie for my flatmate's birthday!",
         "date_published": "2018-03-21 14:07:19", "picture": "apple_pie.jpg"},

        {"author": "1234567j@student.gla.ac.uk",
         "description": "My first try at my mom's pumpkin soup recipe, what do you think?",
         "date_published": "2018-02-09 20:12:34", "picture": "pumpkin_soup.jpg"},

        {"author": "7362514s@student.gla.ac.uk",
         "description": "I tried this recipe for protein pancakes: one egg, one banana, 1/2 cup of oats.",
         "date_published": "2018-02-10 11:20:45", "picture": "pancakes.jpg"},

        {"author": "7382645l@student.gla.ac.uk",
         "description": "Had an ok home-made lamb curry, but I love how the picture turned out!",
         "date_published": "2018-02-15 16:10:03", "picture": "lamb_curry.jpg"},

        {"author": "7382645l@student.gla.ac.uk",
         "description": "I had this amazing paella at my friend's house last night, I think the lighting could have been better",
         "date_published": "2018-03-10 11:10:42", "picture": "paella.jpg"},

        {"author": "jessica09law@fakemail.com",
         "description": "I made an acai bowl at home because they're usually so expensive. It looks sooo good in the picture but I have to say I'm not a fan of acai...",
         "date_published": "2018-02-20 10:33:19", "picture": "acai_bowl.jpg"},

        {"author": "tom_swindon87@fakemail.com",
         "description": "Decided to have a fajita night, and I think the presentation and photo look pretty artsy. Any tips?",
         "date_published": "2018-03-11 19:22:03", "picture": "fajitas.jpg"},

        {"author": "2283116s@student.gla.ac.uk",
         "description": "I tried baking for a change and these blueberry muffins are amazing! Though I think the photo looks a bit plain... What do you think?",
         "date_published": "2018-02-10 15:08:39", "picture": "muffins.jpg"},

        {"author": "jessica09law@fakemail.com",
         "description": """Met up with a friend for coffee and thought I would try taking a typical latte insta pic. """,
         "date_published": "2018-03-01 12:49:04", "picture": "latte.jpg"},

        {"author": "jessica09law@fakemail.com",
         "description": """I made veggie burgers from rice, sweet, potato, black beans and mushrooms. I cooked up all the ingredients, waited for them to cool
         and then shaped them into patties and grilled them on a pan. The great thing about these burgers is that you can pretty much make them out of anything
         you want, and add all the toppings your heart desires! Plus, you’ll be reducing your meat intake, which is not only good for your health, but also the
         environment! Let me know what you think if you try the recipe :)""",
         "date_published": "2018-03-10 20:52:39", "picture": "veggie_burger.jpg"},

        {"author": "7362514s@student.gla.ac.uk",
         "description": """I had this kiwi, apple and spinach smoothie a few weeks ago, it's sweet and great for a hangover ;) The photo is missing a pop of
         colour I think, but I didn't have anything else on hand.""",
         "date_published": "2018-03-19 15:18:43", "picture": "smoothie.jpg"},

        {"author": "tom_swindon87@fakemail.com",
         "description": """Went to Bread Meats Bread for my favourite comfort food: poutine. It's a Canadian dish made of french fries, gravy and cheese curds.
         Super filling but absolutely delicious, and BMB makes a really good one, though heavy on the grave. 9/10 for me :)""",
         "date_published": "2018-03-17 22:03:10", "picture": "poutine.jpg"},

        {"author": "jessica09law@fakemail.com",
         "description": """If you haven't tried rolled ice cream yet, you're missing out!! Went to Rolado this afternoon, on Princes St. It was delicious,
         they have so many flavours on offer and the presentation is so good it's hard to get a bad picture!""",
         "date_published": "2018-03-12 16:33:04", "picture": "ice_cream.jpg"},

        {"author": "jessica09law@fakemail.com",
         "description": """Don't be fooled... I didn't make this from scratch hehe. Love the picture though, so I might post it to instagram. What do you
         think?""",
         "date_published": "2018-03-13 11:45:39", "picture": "mac_cheese.jpg"},
    ]

    reviews = [
        {"author": "7382645l@student.gla.ac.uk", "picture": "2018-03-21 14:07:19", "rating": [2,3,4]},
        {"author": "7362514s@student.gla.ac.uk", "picture": "2018-03-21 14:07:19", "rating": [4,5,1]},
        {"author": "1234567j@student.gla.ac.uk", "picture": "2018-02-10 11:20:45", "rating": [3,4,5]},
        {"author": "7382645l@student.gla.ac.uk", "picture": "2018-02-10 11:20:45", "rating": [5,1,2]},
    ]

    comments = [
        {"author": "7382645l@student.gla.ac.uk", "picture": "2018-03-21 14:07:19",
         "comment": "Looks delicious", "date": "2018-03-21 14:17:21"},
        {"author": "1234567j@student.gla.ac.uk", "picture": "2018-02-10 11:20:45",
         "comment": "Can I have the recipe please =)", "date": "2018-02-10 16:32:21"},
        {"author": "7382645l@student.gla.ac.uk", "picture": "2018-02-10 11:20:45",
         "comment": "I made some just yesterday as well", "date": "2018-02-13 14:20:45"},
    ]

    for user in users:
        author = add_user(user["email"], user["first_name"], user["last_name"], user["date_joined"],
                 user["is_active"], user["is_staff"], user["avatar"], user["password"])

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
                            comment["comment"], comment["date"])


def add_user(email, first_name, last_name, date_joined, is_active, is_staff, avatar, password):
    u = User.objects.get_or_create(email=email)[0]
    u.first_name = first_name
    u.last_name = last_name
    u.date_joined = date_joined
    u.is_active = is_active
    u.is_staff = is_staff
    u.avatar = avatar
    u.set_password(password)
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


def add_comment(author, picture, comment, date):
    com = Comment.objects.get_or_create(author=author, picture=picture)[0]
    com.comment = comment
    com.date_published = date
    com.save()
    return com


if __name__ == '__main__':
     print("Starting Foodgram population script...")
     populate()

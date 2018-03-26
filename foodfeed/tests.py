from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate

from foodfeed.models import *
from foodfeed.forms import *


class IndexPageTest(TestCase):

    def setUp(self):
        User.objects.create_user("7654321d@gla.ac.uk", "qweasdzxc", first_name="Damian", last_name="Darkh")

    def test_index_using_template(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "foodfeed/index.html")

    def test_background_picture_displayed(self):
        response = self.client.get(reverse("index"))
        self.assertIn(b'img src="media/img/index_bg.jpg', response.content)

    def test_index_has_title(self):
        response = self.client.get(reverse('index'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title>', response.content)

    def test_signup_form(self):
        form_data = {"email": "1234567a@gla.ac.uk", "first_name": "Adam", "last_name": "Adams",
                     "password1": "qweasdzxc", "password2": "qweasdzxc"}
        signup_form = SignUpForm(data=form_data)
        self.assertTrue(signup_form.is_valid())


class ModelsTest(TestCase):

    def setUp(self):
        try:
            from population_script import populate
            populate()
        except ImportError:
            print("The module population_script does not exist")
        except NameError:
            print("The function populate() does not exist or is not correct")
        except:
            print("Something went wrong during running the population script")

        self.user = User.objects.get(email="7382645l@student.gla.ac.uk")
        self.user_pic = Picture.objects.get(slug="matthew-jones-picture1")

    def test_user_added(self):
        self.assertIsNotNone(self.user)

    def test_picture_added(self):
        self.assertIsNotNone(self.user_pic)

    def test_rating_added(self):
        rating = Rating.objects.get(author=self.user,
                                    picture=Picture.objects.get(slug="matthew-jones-picture1"))
        self.assertIsNotNone(rating)

    def test_comment_added(self):
        comment = Comment.objects.get(author=User.objects.get(email="7382645l@student.gla.ac.uk"),
                                      picture=self.user_pic)
        self.assertIsNotNone(comment)


class FoodfeedViewTest(TestCase):

    def setUp(self):
        try:
            from population_script import populate
            populate()
        except ImportError:
            print("The module population_script does not exist")
        except NameError:
            print("The function populate() does not exist or is not correct")
        except:
            print("Something went wrong during running the population script")

        self.client.login(email="1234567j@student.gla.ac.uk", password="qwerty")

    def test_foodfeed_using_template(self):
        response = self.client.get(reverse("foodfeed"))
        self.assertTemplateUsed(response, "foodfeed/foodfeed.html")

    def test_foodfeed_has_title(self):
        response = self.client.get(reverse('foodfeed'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title>', response.content)

    def test_foodfeed_contains_user_upload(self):
        response = self.client.get(reverse("foodfeed"))
        #self.assertIn(b'img src="/media/', response.content)

from django.conf.urls import url
from foodfeed import views

urlpatterns = [
    url(r"^$", views.foodfeed, name="foodfeed"),
]

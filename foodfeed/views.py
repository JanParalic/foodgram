from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from foodfeed.forms import SignUpForm, LogInForm
from foodfeed.models import Picture, Rating


def index(request):

    if request.method == "POST":
        sign_up_form = SignUpForm(request.POST)
        login_form = LogInForm(request.POST)

        if sign_up_form.is_valid() and request.POST.get("submit") == "Sign Up":
            sign_up_form.save()
            user_email = sign_up_form.cleaned_data.get("email")
            user_password = sign_up_form.cleaned_data.get("password1")

        elif request.POST.get("submit") == "Login":
            user_email = request.POST.get("email")
            user_password = request.POST.get("password")

        user = authenticate(email=user_email, password=user_password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("foodfeed"))

    else:
        sign_up_form = SignUpForm()
        login_form = LogInForm()

    return render(request, "foodfeed/index.html", {"sign_up_form": sign_up_form,
                                                   "login_form": login_form})


@login_required(login_url="index")
def foodfeed(request):
    feed = Picture.objects.order_by("-date_published")

    if request.method == "POST":
        if request.POST.get("submit") == "Sign Out":
            logout(request)
            return HttpResponseRedirect(reverse("index"))

    return render(request, "foodfeed/foodfeed.html", {"feed": feed})

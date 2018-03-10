from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from foodfeed.forms import SignUpForm, LogInForm
from foodfeed.models import Picture


def index(request):
    registered = False
    logged_in = False

    if request.method == "POST":
        sign_up_form = SignUpForm(request.POST)
        login_form = LogInForm(request.POST)

        if sign_up_form.is_valid() and request.POST.get("submit") == "Sign Up":
            user = sign_up_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

            user_email = user.email
            user_password = sign_up_form.cleaned_data.get("password1")

        elif request.POST.get("submit") == "Login":
            user_email = request.POST.get("email")
            user_password = request.POST.get("password")

        user = authenticate(email=user_email, password=user_password)

        if user:
            if user.is_active:
                login(request, user)
                redirect
                logged_in = True

    else:
        sign_up_form = SignUpForm()
        login_form = LogInForm()

    return render(request, "foodfeed/index.html", {"sign_up_form": sign_up_form,
                                                   "login_form": login_form,
                                                   "registered": registered,
                                                   "logged_in": logged_in})


@login_required(login_url="index")
def foodfeed(request):
    feed = Picture.objects.order_by("-date_published")
    return render(request, "foodfeed/foodfeed.html", {"feed": feed})

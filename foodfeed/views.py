from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse

from foodfeed.forms import *
from foodfeed.models import User, Picture



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
                return redirect("foodfeed")

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
            return redirect("index")

        elif request.POST.get("submit") == "Upload":
            upload_form = ImageUploadForm(request.POST, request.FILES)
            if upload_form.is_valid():
                new_picture = Picture(author=request.user,
                                      picture=request.FILES["picture"],
                                      description=request.POST["description"])
                new_picture.save()
                return redirect("foodfeed")

        elif request.POST.get("submit") == "Comment":
            new_comment = Comment(author=request.user,
                                  picture=Picture.objects.get(slug=request.POST["picture"]),
                                  comment=request.POST["comment"])
            new_comment.save()
            return redirect("foodfeed")

    else:
        upload_form = ImageUploadForm()
        comment_form = CommentSubmissionForm()

    return render(request, "foodfeed/foodfeed.html", {"feed": feed,
                                                      "upload_form": upload_form,
                                                      "comment_form": comment_form})


@login_required(login_url="index")
def profile_edit(request):
    if request.method == "POST":
        profile_edit_form = ProfileEditForm(request.POST, request.FILES)

        for field in profile_edit_form.fields:
            if field != "avatar":
                if request.POST[field] != request.user.__getattr__(field):
                    request.user.__setattr__(field, request.POST[field])
                    request.user.save()
            elif request.FILES.__contains__("avatar"):
                request.user.avatar = request.FILES["avatar"]
                request.user.save()

        return redirect("foodfeed")

    else:
        profile_edit_form = ProfileEditForm(initial={
            "email": request.user.email,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name})

    return render(request, "foodfeed/profile_edit.html", {"form": profile_edit_form})


@login_required(login_url="index")
def user_profile(request, user_name_slug):
    if request.method == "POST":
        if request.POST.get("submit") == "Comment":
            new_comment = Comment(author=request.user,
                                  picture=Picture.objects.get(slug=request.POST["picture"]),
                                  comment=request.POST["comment"])
            new_comment.save()
            return redirect("user_profile", user_name_slug)

    else:
        comment_form = CommentSubmissionForm()

    return render(request, "foodfeed/user_profile.html", {"user": User.objects.get(slug=user_name_slug),
                                                          "comment_form": comment_form})


def about(request):
    return render(request, "foodfeed/about.html")


def make_rating(request):
    if request.is_ajax():
        picture = Picture.objects.get(slug=request.GET.get("picture_slug", ""))
        rating_type = request.GET.get("type", "")
        value = request.GET.get("value", "")

        try:
            rating = Rating.objects.get(author=request.user, picture=picture)

        except:

            rating = Rating.objects.create(author=request.user, picture=picture)

        if rating_type == "health":
            rating.health_rating = value
        elif rating_type == "style":
            rating.style_rating = value
        else:
            rating.cooking_rating = value

        rating.save()
        return True

    else:
        raise Http404

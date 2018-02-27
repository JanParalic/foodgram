from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from foodfeed.forms import SignUpForm

def index(request):
    registered = False
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            registered = True

    else:
        form = SignUpForm()

    return render(request, "foodfeed/index.html", {"form": form, "registered": registered})

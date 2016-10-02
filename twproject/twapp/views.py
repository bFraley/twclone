from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse

# Import the music app models.
from .models import Member, Tweet

# ***************************************
# TODO
# Import Forms
# from .forms import MemberSignupForm
# from .forms import MemberLoginForm
# from .forms import TweetEntryForm

def index(request):
    return render(request, 'twapp/index.html')

# Member data views
def member_list(request):
    members = Member.objects.all()

    context = {
        "members": members,
    }

    return render(request, "twapp/member_list.html", context)


# TODO member_new(request):

# Tweet data views
def tweet_list(request):
    tweets = Tweet.objects.all()
    
    context = {
        "tweets": tweets,
    }

    return render(request, "twapp/tweet_list.html", context)


def signup_form(request):
    return render(request, "twapp/signup_form.html")

def login_form(request):
    return render(request, "twapp/login_form.html")

def posting_form(request):
    return render(request, "twapp/posting_form.html")


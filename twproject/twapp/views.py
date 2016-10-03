from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PostingForm, LoginForm, UserRegistrationForm, MemberForm

# Import the music app models.
from .models import Member, Tweet

def index(request):
    return render(request, 'twapp/index.html')

# Member data views
def member_list(request):
    members = Member.objects.all()

    context = {
        "members": members,
    }

    return render(request, "twapp/member_list.html", context)

def member_tweets(request, id):
    member = Member.objects.filter(id=id)
    tweets = Tweet.objects.filter(memb=id)

    context = {
        "member":member,
        "tweets":tweets
    }
    
    return render(request, 'twapp/member_tweets.html', context)


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
    return render(request, "registration/login.html")

@login_required
def posting_form(request):
    
    if request.method == "POST":
        form = PostingForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.user_id = request.user.id
            new_message.save()
            messages.success(request, 'Message Posted!')
            return redirect('/')
    else:
        form=PostingForm()

    context = {
        "form": form,
    }

    return render(request, "twapp/posting_form.html", context)


def register(request):
    if request.method== "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            new_user = authenticate(username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],)

            login(request, new_user)
            messages.success(request, "User Created!")

            return redirect('twapp:member_tweets')
    else:
        form = UserRegistrationForm()

    context = {
        "form": form
    }
    return render(request, "twapp/signup_form.html", context)

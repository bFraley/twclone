from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

# Import the music app models.
from .models import Member, Tweet, Tag

def index(request):
    return render(request, 'twapp/index.html')

# Member data views
class MemberList(ListView):
    model = Member


class MemberDetail(DetailView):
    model = Member


class MemberCreate(CreateView):
    model = Member
    fields = ('username', 'email')
    template_name = "twapp/index.html"

# Tweet data views
class TweetList(ListView):
    model = Tweet

class TweetDetail(DetailView):
    model = Tweet


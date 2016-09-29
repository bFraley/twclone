from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse

# Import the music app models.
from .models import Member, Tweet, Tag

# ***************************************
# TODO
# Import Forms
# from .forms import MemberSignupForm
# from .forms import MemberLoginForm
# from .forms import TweetEntryForm

def index(request):
    return render(request, 'twapp/index.html')

# Member data views
def  member_list_view(request):
    model = Member


def member_detail_view(request):
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


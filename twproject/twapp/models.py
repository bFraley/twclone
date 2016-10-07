from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import datetime

# Define Tag, Tweet, and Member data models.

# TAGS ARE A BONUS REQUIREMENT
# DON'T DO UNTIL OTHERS ARE DONE
"""
class Tag(models.Model):
    text = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.text
"""

class Member(models.Model):
    account = models.OneToOneField(User)

    def __str__(self):
        return self.account.username

    def get_absolute_url(self):
        return reverse('members:member_detail', kwargs={'id': self.pk})


class Tweet(models.Model):
    memb = models.ForeignKey('Member')
    msg = models.TextField(max_length=140)
    date = datetime.datetime.now()
    # tags = models.ForeignKey('Tag')

    def __str__(self):
        return '{}    {}'.format(self.memb, self.msg)
    
    def get_absolute_url(self):
        return reverse('tweet:tweet_detail', args=[self.pk])

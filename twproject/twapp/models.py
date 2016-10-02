from django.db import models
from django.core.urlresolvers import reverse
import datetime

# Define Tag, Tweet, and Member data models.

# TAGS ARE A BONUS REQUIREMENT
# DON'T DO UNTIL OTHERS ARE DONE
"""
class Tag(models.Model):
    text = models.CharField(max_length=50, null=True)
    
    # NOTE: Here should I just return self.txt ?
    # ******************************************
    def __str__(self):
        return "{}".format(self.text)
"""

class Member(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('members:member_detail', kwargs={'id': self.pk})


class Tweet(models.Model):
    memb = models.ForeignKey('Member', null=True)
    msg = models.TextField(max_length=140)

    # TODO
    # date = " date "
    # tags = models.ForeignKey('Tag')

    def __str__(self):
        return '{}    {}'.format(self.memb, self.msg)
    
    def get_absolute_url(self):
        return reverse('tweet:tweet_detail', args=[self.pk])

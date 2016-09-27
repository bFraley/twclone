from django.db import models
from django.core.urlresolvers import reverse

# Define Member and Tweet data models.

class Member(models.Model):
    username = models.CharField(max_length=20)
    email = models.TextField(max_length=200)

    def __str__(self):
        return '{} {}'.format(self.name, self.email)


class Tweet(models.Model):
    msg = models.TextField(max_length=140)
    date = " date "
    tags = ["#tag1"]

    def __str__(self):
        return '{}    {}    {}'.format(self.msg, self.date, self.tags)
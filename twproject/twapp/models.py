from django.db import models
from django.core.urlresolvers import reverse

# Define Tag, Tweet, and Member data models.

class Tag(models.Model):
    text = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return "{}".format(self.text)

class Member(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return '{} {}'.format(self.username, self.email)

    def get_absolute_url(self):
        return reverse('twapp:member_list', kwargs={'pk': self.pk})


class Tweet(models.Model):
    mem = models.ForeignKey('Member')
    msg = models.TextField(max_length=140)
    date = " date "
    tags = models.ForeignKey('Tag')

    def __str__(self):
        return '{}    {}    {}'.format(self.msg, self.date, self.tags)




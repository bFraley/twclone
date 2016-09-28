from django.contrib import admin

# Import models.
from .models import Member, Tweet, Tag

class TweetAdmin(admin.ModelAdmin):
    list_display = ('msg', 'date', 'tags')


class MemberAdmin(admin.ModelAdmin):
    #search_fields = ('username', 'email')
    list_display = ('username', 'email', ) # get_tweets



admin.site.register(Tweet, TweetAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Tag)


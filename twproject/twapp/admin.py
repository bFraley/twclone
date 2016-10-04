from django.contrib import admin

# Import models.
from .models import Member, Tweet

class TweetAdmin(admin.ModelAdmin):
    list_display = ('memb', 'msg')


class MemberAdmin(admin.ModelAdmin):
    list_display = ('account', )


admin.site.register(Tweet, TweetAdmin)
admin.site.register(Member, MemberAdmin)

from django.contrib import admin

from .models import Community, CommunityMessage

admin.site.register(Community)
admin.site.register(CommunityMessage)

from django.contrib import admin
from foodfeed.models import User, Picture


class UserAdmin(admin.ModelAdmin):

    list_display = ("email", "first_name", "last_name")


admin.site.register(User, UserAdmin)
admin.site.register(Picture)

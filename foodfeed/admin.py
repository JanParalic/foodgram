from django.contrib import admin
from foodfeed.models import User, Picture, Rating, Comment


class UserAdmin(admin.ModelAdmin):

    list_display = ("email", "first_name", "last_name")
    prepopulated_fields = {"slug": ("first_name", "last_name")}


class RatingAdmin(admin.ModelAdmin):

    list_display = ("author", "picture", "health_rating", "style_rating", "cooking_rating")


class CommentAdmin(admin.ModelAdmin):

    list_display = ("author", "picture", "comment")


admin.site.register(User, UserAdmin)
admin.site.register(Picture)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Comment, CommentAdmin)

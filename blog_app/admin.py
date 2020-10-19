from django.contrib import admin
from django.db import models
from . models import Post, Category, Comment,PostViews
from martor.widgets import AdminMartorWidget


class CommentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)
admin.site.register(PostViews)
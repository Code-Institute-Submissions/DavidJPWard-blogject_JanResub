from django.contrib import admin
from .models import Post, Comment, Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'post_date')
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'status', 'post_date')
    search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'post_date', 'approved')
    list_filter = ('approved', 'post_date')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    #list_display=('user_id', 'username', 'email')
    pass
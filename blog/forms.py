from django import forms
from .models import Comment, Post, Profile, User


class CommentForm(forms.ModelForm):
    """
    form for commenting on posts
    """
    class Meta:
        model = Comment
        fields = ('body',)


class CreatePostForm(forms.ModelForm):
    """
    form for creating a post
    """
    class Meta:
        model = Post
        fields = ('title', 'content', 'masthead', 'featured_image', 'category',
                  'status')


class EditUserForm(forms.ModelForm):
    """
    form for editing user infomation
    """
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class EditProfileForm(forms.ModelForm):
    """
    form for editing user profile infomation
    """
    class Meta:
        model = Profile
        fields = ('user_bio',)


class EditPostForm(forms.ModelForm):
    """
    form for editing a post
    """
    class Meta:
        model = Post
        fields = ('title', 'content', 'masthead', 'featured_image', 'category', 'status')

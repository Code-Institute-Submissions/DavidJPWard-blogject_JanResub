from .models import Comment, Post, Profile, User
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'excerpt', 'featured_image', 'category', 'status')


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_bio',)
    
    
class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'excerpt', 'featured_image', 'category',)
"""
veiw classes for project
"""
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post, User
from .forms import (
    CommentForm,
    CreatePostForm,
    EditUserForm,
    EditProfileForm,
    EditPostForm,
)


class PostList(generic.ListView):
    """
    view that handles the home page, getting the list of all posts,
    ordered by most recent and shows them in a list veiw
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-post_date")
    template_name = "index.html"
    paginate_by = 6


class PostLike(View):
    """
    view that handles the liking function, it retreives the post from
    the model and adds the user id to the list of users who have liked
    the post
    """
    def post(self, request, slugParameter):
        post = get_object_or_404(Post, slug=slugParameter)

        if post.likes.filter(id=self.request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(request, "unliked")
        else:
            messages.success(request, "liked")
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse("post_detail",
                                            args=[slugParameter]))


class SubToUser(View):
    """
    view that handles the subscribe function, toggles the user from
    subscribed to unsubscribed from a given user passed in as an argument
    it add the requesting user to the given users 'subscriber list' and adds
    the given user to the requesting users 'subscribed to' list
    """
    def post(self, request, author, slugParameter):
        user = get_object_or_404(User, username=author)
        print(user)
        # messages.info(request, author)
        if user.profile.subscribers.filter(id=self.request.user.id).exists():
            user.profile.subscribers.remove(request.user)
            request.user.profile.subscribed_to.remove(user)
            messages.success(request, f"Unsubscribed to {user}")
        else:
            user.profile.subscribers.add(request.user)
            request.user.profile.subscribed_to.add(user)
            messages.success(request, f"Subscribed to {user}")

        return HttpResponseRedirect(reverse("post_detail", args=[slugParameter]))


class PostDetail(View):
    """
    view that shows the details of a post that a requesting user has clicked on
    """
    def get(self, request, slugParameter, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slugParameter)
        comments = post.comment.filter(approved=True).order_by("post_date")
        # ---likes---
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # ---subs---
        subbed = False
        if post.author.profile.subscribers.filter(id=self.request.user.id).exists():

            subbed = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "subbed": subbed,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slugParameter, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slugParameter)
        comments = post.comment.filter(approved=True).order_by("post_date")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class Profile(View):
    """
    view that shows the profile of a user that the requesting user
    has clicked on
    """
    def get(self, request, user):
        user = get_object_or_404(User, username=user)
        user_posts = Post.objects.filter(author=user)

        subscription_posts = Post.objects.none()
        if user.profile.number_subbed_to() != 0:
            if user.profile.subscribed_to:
                for sub in user.profile.subscribed_to.all():
                    queryset = Post.objects.filter(author=sub)
                    subscription_posts = subscription_posts | queryset

        user_post_paginator = Paginator(user_posts, 3)
        sub_post_paginator = Paginator(subscription_posts, 3)

        page_number = request.GET.get("page")
        user_post_page_obj = user_post_paginator.get_page(page_number)
        sub_post_page_obj = sub_post_paginator.get_page(page_number)

        user_post_pagination = True if user_posts.count() > 3 else False
        sub_post_pagination = True if subscription_posts.count() > 3 else False

        number_of_posts = user_posts.count()

        print(subscription_posts.count())

        context = {
            "user": user,
            "user_post_list": user_post_page_obj,
            "user_post_pagination": user_post_pagination,
            "sub_post_list": sub_post_page_obj,
            "sub_post_pagination": sub_post_pagination,
            "number_of_posts": number_of_posts,
        }
        return render(request, "profile.html", context)


class CreatePost(View):
    """
    view that shows a form that, once submitted, creates a post, only available
    when the user is logged in
    """
    def get(self, request):
        return render(request, "create_post.html", {"form": CreatePostForm})

    def post(self, request):
        create_post_form = CreatePostForm(request.POST, request.FILES)
        if create_post_form.is_valid():
            create_post_form.instance.author = request.user
            post_slug = "".join(
                e for e in create_post_form.instance.title if e.isalnum()
            )
            create_post_form.instance.slug = post_slug
            # create_post_form.instance.featured_image = request.FILES["file"]
            create_post_form.save()
        return redirect("home")


class EditProfile(View):
    """
    view that allows a user to edit their profile, shows both the user form
    and the user profile form.
    """
    def get(self, request):

        edit_user_form = EditUserForm(instance=request.user)
        edit_profile_form = EditProfileForm(instance=request.user.profile)

        return render(
            request,
            "edit_profile.html",
            {"user_form": edit_user_form, "profile_form": edit_profile_form},
        )

    def post(self, request):
        edit_user_form = EditUserForm(request.POST, instance=request.user)
        edit_profile_form = EditProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if edit_user_form.is_valid() and edit_profile_form.is_valid():
            edit_user_form.save()
            edit_profile_form.save()
        return redirect("profile")


class EditPost(View):
    """
    view that allows a user to edit a post they have made.
    """
    def get(self, request, title):
        post_to_edit = get_object_or_404(Post, title=title)

        edit_post_form = EditPostForm(instance=post_to_edit)

        context = {
            "edit_post_form": edit_post_form,
            "post": post_to_edit
        }
        return render(request, "edit_post.html", context)

    def post(self, request, title):
        edit_post_form = EditPostForm(request.POST, request.FILES)
        if edit_post_form.is_valid():
            edit_post_form.save()

        return redirect("profile")

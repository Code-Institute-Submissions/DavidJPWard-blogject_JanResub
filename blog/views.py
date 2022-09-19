from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post, User
from .forms import CommentForm, CreatePostForm, EditUserForm, EditProfileForm

# Create your views here.

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-post_date')
    template_name = 'index.html'
    paginate_by = 6

class PostLike(View):
    def post(self, request, slugParameter):
        post = get_object_or_404(Post, slug=slugParameter)

        if post.likes.filter(id=self.request.user.id).exists():
            #print("unliked")
            post.likes.remove(request.user)
            messages.success(request, "unliked")
        else:
            #print("liked")
            messages.success(request, "liked")
            post.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('post_detail', args=[slugParameter]))
        

class SubToUser(View):
    def post(self, request):
        user = get_object_or_404(User, user=self)

        if user.profile.subscribers.filter(id=self.request.user.id).exists():
            user.profile.subscribers.remove(request.user)
            messages.success(request, "unsubbed")
        else:
            user.profile.subscribers.add(request.user)
            messages.success(request, "unsubbed")

        return HttpResponseRedirect(reverse('post_detail', args=[slugParameter]))



class PostDetail(View):

    def get(self, request, slugParameter, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slugParameter)
        comments = post.comment.filter(approved=True).order_by('post_date')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
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
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slugParameter, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slugParameter)
        comments = post.comment.filter(approved=True).order_by('post_date')
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
                "comment_form": CommentForm()
            }
        )


def Profile(request):
    queryset = Post.objects.filter(author=request.user)

    context = {
        "user": request.user,
        "user_post_list": queryset,
    }
    return render(request, "profile.html", context)


def CreatePost(request):
    if request.POST:
        create_post_form = CreatePostForm(request.POST, request.FILES)
        if create_post_form.is_valid():
            create_post_form.instance.author = request.user
            post_slug = ''.join(e for e in create_post_form.instance.title if e.isalnum())
            create_post_form.instance.slug = post_slug
            #create_post_form.instance.featured_image = request.FILES["file"]
            create_post_form.save()
        return redirect('home')
    return render(request, 'create_post.html', {'form': CreatePostForm})


def EditProfile(request):
    #user = User.objects.filter(user_id=request.user.user_id)


    if request.POST:
        edit_user_form = EditUserForm(request.POST, instance=request.user)
        edit_profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if edit_user_form.is_valid() and edit_profile_form.is_valid():
            edit_user_form.save()
            edit_profile_form.save()
        return redirect('profile')
    
    else:
        edit_user_form = EditUserForm(instance=request.user)
        edit_profile_form = EditProfileForm(instance=request.user.profile)

    return render(request, 'edit_profile.html', {'user_form': edit_user_form, 'profile_form': edit_profile_form})
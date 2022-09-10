from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-post_date')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slugParameter, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slugParameter)
        comments = post.comment.filter(approved=True).order_by('post_date')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            }
        )
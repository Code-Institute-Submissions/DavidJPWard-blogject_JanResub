from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    slug = models.SlugField(max_length=200, unique=True)
    cat_choices = (
        ('Politics','Politics'),
        ('Technology','Technology'),
        ('TV & Film','TV & Film'),
        ('Video Games','Video Games'),
        ('Science','Science'),
        ('Sports','Sports'),
        ('Fashion','Fashion'),
        ('Music','Music'),
    )
    category = models.CharField(max_length=30, blank=True, null=True, choices=cat_choices)





    class Meta:
        ordering = ['-post_date']
    
    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField(max_length=300)
    post_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image', default='profile_placeholder')
    slug = models.SlugField(max_length=200)
    subscribers = models.ManyToManyField(User, related_name='subs', blank=True)

    def __str__(self):
        return self.user.username
        
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('createpost/', views.CreatePost, name='create_post'),
    path('<slug:slugParameter>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slugParameter>', views.PostLike.as_view(), name='post_like'),


]
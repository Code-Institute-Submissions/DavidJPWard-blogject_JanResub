from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('editpost/<str:title>', views.EditPost.as_view(), name='edit_post'),
    path('delete/<slug:slugParameter>', views.DeletePost.as_view(), name='delete_post'),
    path('user/edit/', views.EditProfile.as_view(), name='edit_profile'),
    path('createpost/', views.CreatePost.as_view(), name='create_post'),
    path('<slug:slugParameter>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slugParameter>', views.PostLike.as_view(), name='post_like'),
    path('sub/<str:author>/<slug:slugParameter>', views.SubToUser.as_view(), name='sub_to_user'),
    path('user/<str:user>', views.Profile.as_view(), name='profile'),
]

from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slugParameter>/', views.PostDetail.as_view(), name='post_detail'),
]
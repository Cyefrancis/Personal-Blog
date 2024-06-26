from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from blog.views import PostList, Details, CreatePost, EditPost, DeletePost, Home


urlpatterns = [
    path('posts/new', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/edit/', EditPost.as_view(), name='post_edit'),
    path('post/<int:pk>/', Details.as_view(), name='post_detail'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('delete_post/', DeletePost.as_view()),
    path('home/', Home.as_view(), name='home'),
]

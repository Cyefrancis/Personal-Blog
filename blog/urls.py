from django.urls import path
from django.views.generic import TemplateView
from blog.views import PostList, Details, CreatePost, EditPost, DeletePost

urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
    path('details/', Details.as_view(), name='details'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('edit_post/', EditPost.as_view(), name='edit_post'),
    path('delete_post/', DeletePost.as_view())
]

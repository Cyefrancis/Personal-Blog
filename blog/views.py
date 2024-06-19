from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post
# Create your views here.


class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class Details(TemplateView):
    template_name = 'post_detail.html'

class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'form_create.html'
    success_url = reverse_lazy('post_list')

class EditPost(TemplateView):
    template_name = 'edit_post.html'

class DeletePost(TemplateView):
    template_name = 'delete_post.html'
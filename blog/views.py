from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post
# Create your views here.


class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-created_date')

class Details(TemplateView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'posts'

class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'form_create.html'
    success_url = reverse_lazy('post_list')

class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'form_create.html'
    success_url = reverse_lazy('post_list')

    """ def get_success_url(self):
        return reverse_lazy('post_list', kwargs= {'pk': self.object.pk}) """

class DeletePost(TemplateView):
    template_name = 'delete_post.html'

class Home(TemplateView):
    template_name = 'home.html'
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy, reverse
from .forms import PostForm, RegisterForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
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

class Login():
    pass

def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
        #log the user in after registration
            new_user = authenticate(username=user.username, password= form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

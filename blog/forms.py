from django.forms import ModelForm
from django import forms
from blog.models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','author']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

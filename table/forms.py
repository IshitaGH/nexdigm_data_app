from django import forms
from django.forms import ModelForm
from .models import Post

class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
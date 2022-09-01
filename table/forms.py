from django import forms
from django.forms import ModelForm
from .models import Post

class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = ('num1', 'num2', 'Year', 'Month', 'File_Type', 'Consolidation_Type')
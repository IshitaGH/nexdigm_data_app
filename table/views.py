from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
from django.views.generic import CreateView, DetailView

# Create your views here.

# def home(request):
#     model = Post
#     fields = ['num1', 'num2']
#     template_name = 'table/home.html'
#     context_object_name = 'posts'

#     return render(request, 'table/home.html')

class PostCreateView(CreateView):
    model = Post
    fields = ['num1', 'num2']

class PostDetailView(DetailView):
    model = Post
    # return render(request, 'table/output.html', {'title': 'About'})
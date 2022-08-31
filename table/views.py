from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
from django.views.generic import CreateView, DetailView
from scripts.dummy_script import dummy
from .forms import Post_Form
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    # model = Post
    # fields = ['num1', 'num2']
    # template_name = 'table/home.html'
    # context_object_name = 'posts'

    submitted = False
    if request.method == "POST":
        form = Post_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('output/')
    else:
        form = Post_Form
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'table/home.html', {'form':form, 'submitted':submitted})

def output(request):
    current = Post.objects.last()
    out = dummy(current.num1, current.num2)
    return render(request, 'table/output.html', {'out':out})

def about(request):
    return render(request, 'table/about.html', {'title': 'About'})

# class PostCreateView(CreateView):
#     model = Post
#     fields = ['num1', 'num2']

# class PostDetailView(DetailView):
#     model = Post
#     # num_in_db = Post.pk
#     # int:num_in_db
#     # print(num_in_db)
#     current = Post.objects.last()
#     print(current)
#     # attributes = dir(model)
#     # print(attributes)
#     print('sup')
#     out = dummy(current.num1, current.num2)
#     context = { out }
#     # return render(request, 'table/output.html', {'title': 'About'})
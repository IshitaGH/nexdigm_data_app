from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post, Data
# from django.views.generic import CreateView, DetailView
from .forms import Post_Form
from django.http import HttpResponseRedirect
import runpy
from django.contrib.auth.decorators import login_required
from django_tables2 import SingleTableView
from .tables import Currency_Master, Product_Master, Distributor_Master
# Create your views here.

@login_required
def home(request):
    # model = Post
    # fields = ['num1', 'num2']
    # template_name = 'table/home.html'
    # context_object_name = 'posts'

    submitted = False
    if request.method == "POST":
        form = Post_Form(request.POST)
        if form.is_valid():
            new_post = form.save()
            new_post.author = request.user
            new_post.save()
            return HttpResponseRedirect('output/')
    else:
        form = Post_Form
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'table/home.html', {'form':form, 'submitted':submitted})

# output = [
#     'sum' = 
# ]

@login_required
def output(request):
    current = Post.objects.filter(author=request.user).last()
    if not current:
        return HttpResponseRedirect('/')
    else:
        global_vars = {
            "current_entry": current
        }
        runpy.run_path(path_name=r"../nexdigm_data_app/scripts/run_scripts.py", init_globals=global_vars, run_name='__main__')
        
        context = {
            "add": current.add,
            "square": current.square,
            "neg": current.neg
        }
        return render(request, 'table/output.html', context)

def about(request):
    return render(request, 'table/about.html', {'title': 'About'})

class CurrencyTableView(SingleTableView):
    model = Data
    table_class = Currency_Master
    template_name = 'table/tables.html'

class ProductTableView(SingleTableView):
    model = Data
    table_class = Product_Master
    template_name = 'table/tables.html'

class DistributorTableView(SingleTableView):
    model = Data
    table_class = Distributor_Master
    template_name = 'table/tables.html'

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
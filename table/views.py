from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import Post, Data
from users.models import Profile
# from django.views.generic import CreateView, DetailView
from .forms import Post_Form, Data_Form, Data_FormSet
from django.http import HttpResponseRedirect
import runpy
from django.contrib.auth.decorators import login_required
from django_tables2 import SingleTableView
from .tables import Currency_Master, Product_Master, Distributor_Master
from django.forms import modelformset_factory
# Create your views here.

@login_required
def home(request):
    # model = Post
    # fields = ['num1', 'num2']
    # template_name = 'table/home.html'
    # context_object_name = 'posts'

    for p in Profile.objects.all():
        print(p)
        print()
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

def create_data(request, pk, which_master):
    author = Profile.objects.get(user=request.user)
    d = Data.objects.filter(author=author)
    form = Data_Form(request.POST or None)
    print("in create data\n")

    if request.method == "POST":
        print("in request.method=POST of create_data")
        if form.is_valid():
            data = form.save(commit=False)
            data.author = author
            data.save()
            print("create data redirecting to detail data\n")
            return redirect("detail-data", pk=data.id)
        else:
            print("create data redirecting to create data cuz invalid form\n")
            return render(request, "table/partials/data_form.html", context={
                "form": form
            })

    context = {
        "form": form,
        "author": author,
        "data": d
    }
    print("create data redirecting to create cuz nothing happened data\n")

    return render(request, "table/create_data.html", context)

def update_data(request, pk, which_master):
    print(f'pk passed into fn: {pk}')
    data = Data.objects.get(pk=pk)
    print(f'data referenced: {data}\n')
    form = Data_Form(request.POST or None, instance=data)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            print("in update data- when updating data IS posted, id available")
            print(data.id)
            return redirect("detail-data", pk=data.pk)

    context = {
        "form": form,
        "d": data,
    }

    print("in update data- data form NOT yet posted")
    return render(request, "table/partials/data_form.html", context)

def delete_data(request, pk):
    data = get_object_or_404(Data, pk=pk)

    if request.method == "POST":
        data.delete()
        print("in delete data- deleted entry")
        return HttpResponse("")

    print("in delete data- did not delete the data")
    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )

def detail_data(request, pk, which_master):
    data = get_object_or_404(Data, pk=pk)
    print(data.pk)
    print("in detail data, detail id is ^\n\n")
    context = {
        "d": data,
    }
    if which_master == 0:
        return render(request, "table/partials/currency_data_detail.html", context)
    if which_master == 1:
        return render(request, "table/partials/product_data_detail.html", context)
    if which_master == 2:
        return render(request, "table/partials/base_data_detail.html", context)

def create_data_form(request):
    form = Data_Form()
    context = {
        "form": form
    }
    print("in create data form- am creating a new data entry\n\n")
    return render(request, "table/partials/data_form.html", context)
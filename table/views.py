from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from .models import Post, Data
from users.models import Profile
from .forms import Post_Form, Data_Form
import runpy
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    submitted = False
    if request.method == "POST":
        # if the user clicks submit, validate and save the form, then redirect to the output page
        form = Post_Form(request.POST)
        if form.is_valid():
            new_post = form.save()
            new_post.author = request.user
            new_post.save()
            return HttpResponseRedirect('output/')
    else:
        # if the user has not yet submitted, then stay on the home page
        form = Post_Form
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'table/home.html', {'form':form, 'submitted':submitted})

@login_required
def output(request):
    # get the most recent output for each user
    current = Post.objects.filter(author=request.user).last()
    
    if not current:
        # if the user has not filled out the Post_Form before and navigated to this page by themselves,
        # send them back to the home page
        return HttpResponseRedirect('/')
    else:
        # run the dummy scripts and display the output
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

# display the about page for the website
def about(request):
    return render(request, 'table/about.html', {'title': 'About'})

@login_required
def create_data(request, pk, which_master):
    author = Profile.objects.get(user=request.user)
    d = Data.objects.filter(author=author)
    form = Data_Form(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            # if the user inputted valid data, save it and redirect it to the normal master data page
            data = form.save(commit=False)
            data.author = author
            data.save()
            return redirect("detail-data", pk=data.id, which_master=which_master)
        else:
            # if the user inputted invalid data, tell them they need to submit valid data
            return render(request, "table/partials/data_form.html", context={
                "form": form
            })

    context = {
        "form": form,
        "author": author,
        "data": d,
        "which_master": which_master
    }

    # if the user is not adding new data, then display the normal master data page
    return render(request, "table/create_data.html", context)

@login_required
def update_data(request, pk, which_master):
    data = Data.objects.get(pk=pk)
    form = Data_Form(request.POST or None, instance=data)

    # if the user updates the data and it is valid, then save the changes and go back to the normal master data page
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("detail-data", pk=data.pk, which_master=which_master)

    # if the user has not yet updated the data or it is not valid, keep showing them the form to update
    context = {
        "form": form,
        "d": data,
        "which_master": which_master
    }

    return render(request, "table/partials/data_form.html", context)

@login_required
def delete_data(request, pk):
    # delete the data object if they click delete
    data = get_object_or_404(Data, pk=pk)

    if request.method == "POST":
        data.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )

@login_required
def detail_data(request, pk, which_master):
    # depending on which master data page they are accessing, display the pertinent information
    # eg. if in currency master data, display currency, but not product information
    data = get_object_or_404(Data, pk=pk)
    context = {
        "d": data,
        "which_master": which_master
    }
    if which_master == 0:
        return render(request, "table/partials/currency_data_detail.html", context)
    if which_master == 1:
        return render(request, "table/partials/product_data_detail.html", context)
    if which_master == 2:
        return render(request, "table/partials/base_data_detail.html", context)

@login_required
def create_data_form(request):
    # display the form for creating a new data object
    form = Data_Form()
    context = {
        "form": form,
    }
    return render(request, "table/partials/data_form.html", context)
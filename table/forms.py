from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Post, Data
from users.models import Profile
from django.contrib.auth.models import User

#define the form for the meta-information in the home page
class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = ('num1', 'num2', 'Year', 'Month', 'File_Type', 'Consolidation_Type')

#define the form for the data records in the master data pages
class Data_Form(ModelForm):
    class Meta:
        model = Data
        fields = ('Distributor', 'Region', 'Name', 'Selection', 'Currency', 'Product')
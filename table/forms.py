from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Post, Data
from users.models import Profile
from django.contrib.auth.models import User

class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = ('num1', 'num2', 'Year', 'Month', 'File_Type', 'Consolidation_Type')

class Data_Form(ModelForm):
    class Meta:
        model = Data
        fields = ('Distributor', 'Region', 'Name', 'Selection', 'Currency', 'Product')

class Distributor_Data_Form(ModelForm):
    class Meta:
        model = Data
        fields = ('Distributor', 'Region', 'Name', 'Selection', 'Currency', 'Product')

class Currency_Data_Form(ModelForm):
    class Meta:
        model = Data
        fields = ('Distributor', 'Region', 'Name', 'Selection', 'Currency', 'Product')

class Product_Data_Form(ModelForm):
    class Meta:
        model = Data
        fields = ('Distributor', 'Region', 'Name', 'Selection', 'Currency', 'Product')


Data_FormSet = inlineformset_factory(
    Profile,
    Data,
    Data_Form,
    can_delete=False,
    min_num=2,
    extra=0,
)
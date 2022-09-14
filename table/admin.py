from django.contrib import admin
from .models import Post, Data
from users.models import Profile
# Register your models here.

class DataInLineAdmin(admin.TabularInline):
    model = Data

# class ProfileAdmin(admin.ModelAdmin):
#     inlines=[DataInLineAdmin]

admin.site.register(Post)
admin.site.register(Data)
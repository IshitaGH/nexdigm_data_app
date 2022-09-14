from django.contrib import admin
from .models import Profile
from table.admin import DataInLineAdmin

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    inlines=[DataInLineAdmin]

admin.site.register(Profile, ProfileAdmin)

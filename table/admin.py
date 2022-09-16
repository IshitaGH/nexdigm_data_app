from django.contrib import admin
from .models import Post, Data
from users.models import Profile
# Register your models here.

# lets all of the data records associated with a user to be displayed under the user in admin
class DataInLineAdmin(admin.TabularInline):
    model = Data

admin.site.register(Post)
admin.site.register(Data)
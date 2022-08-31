from django.urls import path
from . import views
# from .views import PostCreateView, PostDetailView

urlpatterns = [
    path('', views.home, name='table-home'),
    path('output/', views.output, name="table-output/"),
]
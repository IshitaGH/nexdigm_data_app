from django.urls import path
from . import views
from .views import PostCreateView, PostDetailView

urlpatterns = [
    path('', PostCreateView.as_view(), name='table-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail/"),
]
from django.urls import path
from . import views
from .views import CurrencyTableView, ProductTableView
# from .views import PostCreateView, PostDetailView

urlpatterns = [
    path('', views.home, name='table-home'),
    path('output/', views.output, name="table-output/"),
    path('about/', views.about, name='table-about'),
    path('currency_master_data/', CurrencyTableView.as_view(), name='table-currency-master-data'),
    path('product_master_data/', ProductTableView.as_view(), name='table-product-master-data'),
    path('distributor_master_data/<pk>/', views.create_data, name='table-distributor-create-data'),
    path('htmx/data/<pk>/', views.detail_data, name="detail-data"),
    path('htmx/data/<pk>/update/', views.update_data, name="update-data"),
    path('htmx/data/<pk>/delete/', views.delete_data, name="delete-data"),
    path('htmx/create-data-form/', views.create_data_form, name='create-data-form'),
]
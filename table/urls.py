from django.urls import path
from . import views
from .views import CurrencyTableView, ProductTableView, DistributorTableView
# from .views import PostCreateView, PostDetailView

urlpatterns = [
    path('', views.home, name='table-home'),
    path('output/', views.output, name="table-output/"),
    path('about/', views.about, name='table-about'),
    path('currency_master_data/', CurrencyTableView.as_view(), name='table-currency-master-data'),
    path('product_master_data/', ProductTableView.as_view(), name='table-product-master-data'),
    path('distributor_master_data/', DistributorTableView.as_view(), name='table-distributor-master-data'),
]
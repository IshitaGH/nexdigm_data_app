from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='table-home'),
    path('output/', views.output, name="table-output/"),
    path('about/', views.about, name='table-about'),
    path('master_data/<int:which_master>/<pk>/', views.create_data, name='table-master-create-data'),
    # the htmx urls allow the master data pages to dynamically display data without rerendering the page
    path('htmx/data/<pk>/<int:which_master>/', views.detail_data, name="detail-data"),
    path('htmx/data/<pk>/update/<int:which_master>/', views.update_data, name="update-data"),
    path('htmx/data/<pk>/delete/', views.delete_data, name="delete-data"),
    path('htmx/create-data-form/', views.create_data_form, name='create-data-form'),
]
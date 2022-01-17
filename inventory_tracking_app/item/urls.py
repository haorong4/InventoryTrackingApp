from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('delete/<int:pk>/', views.item_delete, name='item-delete'),
    path('edit/<int:pk>/', views.item_edit, name='item-edit'),
    path('export', views.export_csv, name='export_csv'),
]
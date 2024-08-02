# urls.py

from django.urls import path
from .views import EmpListCreateView, EmpDetailView

urlpatterns = [
    path('employees/', EmpListCreateView.as_view(), name='emp-list-create'),
    path('employees/<int:pk>/', EmpDetailView.as_view(), name='emp-detail'),
]

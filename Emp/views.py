# myapp/views.py

from rest_framework import generics
from .models import Emp
from .serializers import EmpSerializer


class EmpListCreateView(generics.ListCreateAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

class EmpDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
# views.py
from rest_framework import generics
from .models import Emp
from .serializers import EmpSerializer

class EmpListCreateView(generics.ListCreateAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

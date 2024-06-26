# branch/views.py
from rest_framework import generics
from .models import Branch
from .serializers import BranchSerializer

class BranchListCreateView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

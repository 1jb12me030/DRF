from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Candidate
from .serializers import CandidateDirectorySerializer

class CandidateListCreateView(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateDirectorySerializer

class CandidateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateDirectorySerializer

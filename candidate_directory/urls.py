from django.urls import path
from .views import CandidateListCreateView, CandidateDetailView

urlpatterns = [
    path('candidates/', CandidateListCreateView.as_view(), name='candidate-list-create'),
    path('candidates/<int:pk>/', CandidateDetailView.as_view(), name='candidate-detail'),
]

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Experience
from .serializers import ExperienceSerializer


class ExperienceViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        Experience.objects.all()
    )

    serializer_class = (
        ExperienceSerializer
    )
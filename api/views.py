from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ContactDetailSerializer
from .models import ContactDetail

# Create your views here.

class ContactDetailViewSet(viewsets.ModelViewSet):
    queryset = ContactDetail.objects.all()
    serializer_class = ContactDetailSerializer
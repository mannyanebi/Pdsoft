from rest_framework import serializers

from .models import ContactDetail

class ContactDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactDetail
        fields = ('fullname', 'email', 'message')
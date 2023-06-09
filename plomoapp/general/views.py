from rest_framework import viewsets, permissions
from general.models import Contacto
from general.serializers import ContactoSerializador


class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializador    

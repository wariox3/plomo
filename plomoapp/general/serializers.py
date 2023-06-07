from general.models import Contacto, Ciudad
from rest_framework import serializers

class CiudadSerializador(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ciudad
        fields = [
            'nombre'
            ] 

class ContactoSerializador(serializers.HyperlinkedModelSerializer):
    ciudad = serializers.PrimaryKeyRelatedField(queryset=Ciudad.objects.all())

    class Meta:
        model = Contacto
        fields = [
            'numero_identificacion',
            'nombre_corto',
            'ciudad',
            ]

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'nombre_corto': instance.nombre_corto
        }
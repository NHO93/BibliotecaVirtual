from rest_framework import serializers
from .models import Colecao

class ColecaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colecao
        fields = '__all__'
        read_only_fields = ['colecionador']

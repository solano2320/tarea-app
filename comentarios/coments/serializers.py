from rest_framework import serializers
from .models import Coments

#creamos el serializador
class ComentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Coments
        fields = ["name", "email", "coment","date"] 

    
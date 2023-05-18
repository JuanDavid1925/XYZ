from rest_framework import serializers
from .models import User

# Paso de los datos del modelo a json
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
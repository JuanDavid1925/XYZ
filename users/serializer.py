from django.contrib.auth import get_user_model
from rest_framework import serializers

userModel = get_user_model()

# Paso de los datos del modelo a json
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = userModel
        fields = '__all__'
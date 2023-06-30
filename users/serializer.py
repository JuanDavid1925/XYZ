from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

userModel = get_user_model()

# Paso de los datos del modelo a json
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = userModel
        fields = '__all__'

class UserListSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = userModel
        fields = ('id', 'username', 'is_active', 'is_staff', 'password')


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = userModel
        fields = '__all__'
    def create(self, data):
        user = userModel.objects.create_user(username=data['username'], password=data['password'])
        user.save()


class UserLoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()
	##
	def check_user(self, data):
		user = authenticate(username=data['username'], password=data['password'])
		if not user:
			raise ValueError('user not found')
		return user
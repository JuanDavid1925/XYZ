from rest_framework import viewsets, permissions, status
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer
from .models import User

userModel = get_user_model()

# Create your views here.
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        username = data[username]
        password = data[password]

        user = userModel.objects.create_user(username, password)
        user = UserSerializer(user)

        return Response(user.data, status=status.HTTP_201_CREATED)


class RetrieveUserView():
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        pass
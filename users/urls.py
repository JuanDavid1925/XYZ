from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import UserView, RegisterView, LoginView, LogoutView,UsersListView
from rest_framework.documentation import include_docs_urls
from django.urls import path

urlpatterns = [
    path('XYZ-api/v1/user/', UserView.as_view()),
    path('XYZ-api/v1/register/', RegisterView.as_view()),
    path('XYZ-api/v1/login/', LoginView.as_view()),
    path('XYZ-api/v1/logout/', LogoutView.as_view()),
    path('users-crud-docs/', include_docs_urls(title='Users API')),
    path('user-list/',UsersListView.as_view())
]
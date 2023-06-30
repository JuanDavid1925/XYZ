from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import UserView, RegisterView, LoginView, LogoutView
from rest_framework.documentation import include_docs_urls
from django.urls import path

urlpatterns = [
    path('XYZ-api/v1/user/', UserView.as_view()),
    path('XYZ-api/v1/register/', RegisterView.as_view()),
    path('XYZ-api/v1/login/', LoginView.as_view()),
    path('XYZ-api/v1/logout/', LogoutView.as_view()),
    path('XYZ-api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('XYZ-api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('XYZ-api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users-crud-docs/', include_docs_urls(title='Users API'))
]
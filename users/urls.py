from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.documentation import include_docs_urls
from .views import UserView, RegisterView
from django.urls import path, include
from rest_framework import routers

# Acceso a la api
router = routers.DefaultRouter()
router.register(r'users', UserView, 'users')

urlpatterns = [
    path('XYZ-api/v1/users', include(router.urls)),
    path('XYZ-api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('XYZ-api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('XYZ-api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users-crud-docs/', include_docs_urls(title='Users API')),
    path('register/', RegisterView.as_view())
]
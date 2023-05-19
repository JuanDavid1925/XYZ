from rest_framework.documentation import include_docs_urls
from django.urls import path, include
from rest_framework import routers
from users import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# Acceso a la api
router = routers.DefaultRouter()
router.register(r'users', views.UserView, 'users')

urlpatterns = [
    path('XYZ-api/v1/', include(router.urls)),
    path('XYZ-api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('XYZ-api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('XYZ-api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users-crud-docs/', include_docs_urls(title='Users API'))
]
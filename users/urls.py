from rest_framework.documentation import include_docs_urls
from django.urls import path, include
from rest_framework import routers
from users import views

# Acceso a la api
router = routers.DefaultRouter()
router.register(r'users', views.UserView, 'users')

urlpatterns = [
    path('XYZ-api/v1/', include(router.urls)),
    path('users-crud-docs/', include_docs_urls(title='Users API'))
]
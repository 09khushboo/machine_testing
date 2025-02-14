from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet
from .views import edit_client, delete_client

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('clients/<int:client_id>/edit/', edit_client, name='edit_client'),
    path('clients/<int:client_id>/delete/', delete_client, name='delete_client'),
]

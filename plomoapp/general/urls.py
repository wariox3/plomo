from django.urls import path, include
from .views import ContactoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'contacto', ContactoViewSet)


urlpatterns = [    
    path('', include(router.urls)),
]
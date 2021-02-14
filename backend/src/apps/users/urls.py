from django.urls import path, include
from rest_framework import routers
from .views import User_detail_view

router = routers.DefaultRouter()
router.register(r'', User_detail_view)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework import routers
from .views import Task_detail_view

router = routers.DefaultRouter()
router.register(r'', Task_detail_view)

urlpatterns = [
    path('', include(router.urls)),
]
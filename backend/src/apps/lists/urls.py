from django.urls import path, include
from rest_framework_nested import routers
from .views import List_detail_view, List_item_detail_view

router = routers.SimpleRouter()
router.register(r'', List_detail_view)

items_router = routers.NestedSimpleRouter(router, r'', lookup='list')
items_router.register(r'', List_item_detail_view, basename='items')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(items_router.urls)),
]
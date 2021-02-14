from django.urls import path, include
from rest_framework_nested import routers
from .views import User_detail_view
from ..tasks.views import Task_detail_view
from ..lists.views import List_detail_view, List_item_detail_view

router = routers.SimpleRouter()
router.register(r'', User_detail_view, basename='users')

task_router = routers.NestedSimpleRouter(router, r'', lookup='users')
task_router.register(r'', Task_detail_view, basename='tasks')

list_router = routers.NestedSimpleRouter(router, r'', lookup='users')
list_router.register(r'', List_detail_view, basename='lists')

items_router = routers.NestedSimpleRouter(list_router, r'', lookup='lists')
items_router.register(r'', List_item_detail_view, basename='items')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(task_router.urls)),
    path('', include(list_router.urls)),
    path('', include(items_router.urls)),
]
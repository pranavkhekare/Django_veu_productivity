from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model
from .models import List, List_items


# Create serializer to define API representation
class List_serializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())

    class Meta:
        model = List
        fields = ['list_name', 'description', 'user_id', 'created_at', 'updated_at']


# Create your views here.
class List_detail_view(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = List_serializer


class List_item_serializer(serializers.HyperlinkedModelSerializer):
    parent_list = serializers.PrimaryKeyRelatedField(queryset=List.objects.all())

    class Meta:
        model = List_items
        fields = ['text', 'parent_list', 'created_at', 'updated_at']


class List_item_detail_view(viewsets.ModelViewSet):
    queryset = List_items.objects.all()
    serializer_class = List_item_serializer

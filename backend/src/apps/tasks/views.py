from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model
from.models import Task


# Create serializer to define API representation
class Task_serializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())

    class Meta:
        model = Task
        fields = ['title', 'description', 'user_id', 'created_at', 'updated_at']


# Create your views here.
class Task_detail_view(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = Task_serializer

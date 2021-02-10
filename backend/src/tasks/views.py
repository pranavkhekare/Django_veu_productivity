from rest_framework import serializers, viewsets
from.models import Task


# Create serializer to define API representation
class Task_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'created_at', 'updated_at']


# Create your views here.
class Task_detail_view(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = Task_serializer

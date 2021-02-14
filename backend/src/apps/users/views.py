from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model
from .models import User


# Create your views here.
class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class User_detail_view(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_serializer

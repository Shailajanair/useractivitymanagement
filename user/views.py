from rest_framework import viewsets
from user.models import CustomUser, ActivityDetail
from user.serializers import CustomUserSerializer, ActivityDetailSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class ActivityDetailViewSet(viewsets.ModelViewSet):
    serializer_class = ActivityDetailSerializer
    queryset = ActivityDetail.objects.all()

from rest_framework import viewsets
from user.models import CustomUser, ActivityDetail
from user.serializers import CustomUserSerializer, ActivityDetailSerializer
from rest_framework.response import Response


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    def list(self, request, *args, **kwargs):
        serialized_data = CustomUserSerializer(self.queryset, many=True).data
        return Response({"ok": "true", "members": serialized_data})


class ActivityDetailViewSet(viewsets.ModelViewSet):
    serializer_class = ActivityDetailSerializer
    queryset = ActivityDetail.objects.all()

from django.urls import path, include
from rest_framework import routers

from user import views

router = routers.DefaultRouter()
router.register('custom_user', views.CustomUserViewSet)
router.register('activity_period', views.ActivityDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


from django.contrib.auth.models import AbstractUser
from django.db import models
import pytz


class CustomUser(AbstractUser):
    system_id = models.CharField(max_length=64)
    timezone = models.CharField(max_length=120, choices=[(timezone, timezone) for timezone in pytz.common_timezones],)


class ActivityDetail(models.Model):
    custom_user = models.ManyToManyField(CustomUser)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

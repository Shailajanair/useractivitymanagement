from django.contrib.auth.models import AbstractUser
from django.db import models
import pytz


class CustomUser(AbstractUser):
    system_id = models.CharField(max_length=64)
    timezone = models.CharField(max_length=120, choices=[(timezone, timezone) for timezone in pytz.common_timezones],)

    def __str__(self):
        return self.system_id + ' : ' + self.timezone

    class Meta:
        db_table = 'custom_user'


class ActivityDetail(models.Model):
    custom_user = models.ManyToManyField(CustomUser)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'activity_detail'

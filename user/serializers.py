from rest_framework import serializers
from user.models import CustomUser, ActivityDetail


class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    activity_periods = serializers.SerializerMethodField()
    real_name = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.system_id

    def get_activity_periods(self, obj):
        return ActivityDetailSerializer(obj.activitydetail_set.all(), many=True).data

    def get_real_name(self, obj):
        return obj.first_name + " " + obj.last_name

    class Meta:
        model = CustomUser
        fields = ('id', 'real_name', 'timezone', 'activity_periods')


class ActivityDetailSerializer(serializers.ModelSerializer):
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()

    def get_start_time(self, obj):
        return obj.start_time.strftime('%b %-d %Y %-I:%M%p')

    def get_end_time(self, obj):
        return obj.end_time.strftime('%b %-d %Y %-I:%M%p')

    class Meta:
        model = ActivityDetail
        fields = ('start_time', 'end_time')

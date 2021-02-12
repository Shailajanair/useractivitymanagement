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
        fields = ('id', 'activity_periods', 'real_name', 'timezone')


class ActivityDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityDetail
        fields = ('start_date', 'end_date')

from datetime import datetime
import random
import string
import names
from django.core.management.base import BaseCommand
from user.models import CustomUser
import pytz


class Command(BaseCommand):
    help = 'Creates custom users'

    def handle(self, *args, **kwargs):
        for i in range(0, 10):
            # choosing random system_id, username etc to populate database
            system_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
            if CustomUser.objects.filter(system_id=system_id).exists():
                continue
            time_zone = random.choices(pytz.common_timezones)[0]
            firstname, lastname = names.get_first_name(), names.get_last_name()
            username = firstname + lastname
            custom_obj = CustomUser.objects.create(first_name=firstname, last_name=lastname, username=username,
                                                   system_id=system_id, timezone=time_zone)
            for j in range(0, 3):
                # end time should always be greater than start time
                random_year, random_month, random_date = random.randint(2000, 2021), random.randint(1, 12), random.randint(1, 25)
                random_hour, random_hour_2, random_min, random_min_2 = random.randint(0, 12), random.randint(0, 12),\
                                                                         random.randint(0, 59), random.randint(0, 59)
                start_time_minute, end_time_minute = min(random_min, random_min_2), max(random_min, random_min_2)
                start_time_hour, end_time_hour = min(random_hour, random_hour_2), max(random_hour, random_hour_2)

                start_time, end_time = datetime(random_year, random_month, random_date, start_time_hour, start_time_minute, 00),\
                                       datetime(random_year, random_month, random_date, end_time_hour, end_time_minute, 00)

                custom_obj.activitydetail_set.create(start_time=start_time, end_time=end_time)
        return

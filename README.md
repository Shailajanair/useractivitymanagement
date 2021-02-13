**PROJECT AIM**

Design and implement a Django application with User and ActivityPeriod models, write  a custom management command
to populate the database with some dummy data, and design an API to serve that data in the json format.

**PACKAGES USED**
```
asgiref==3.3.1
Django==3.1.6
djangorestframework==3.12.2
pytz==2021.1
sqlparse==0.4.1
names==0.3.0
```
**CUSTOM MANAGEMENT COMMAND TO POPULATE DATABASE**

`./manage.py create_users`

**API ENDPOINT**
`http://shailajanair.pythonanywhere.com/user/custom_user/`

**SAMPLE RESPONSE**
```
[
  {
    "id": "KLEMLQ713",
    "real_name": "Julio Strain",
    "timezone": "Indian/Maldives",
    "activity_periods": [
      {
        "start_time": "Jul 10 2010 9:36AM",
        "end_time": "Jul 10 2010 3:40PM"
      },
      {
        "start_time": "Feb 4 2019 12:37PM",
        "end_time": "Feb 4 2019 3:47PM"
      },
      {
        "start_time": "Sep 16 2008 9:43AM",
        "end_time": "Sep 16 2008 12:53PM"
      }
    ]
  },
  {
    "id": "I4E3KRNUX",
    "real_name": "Brenda Jackson",
    "timezone": "Pacific/Funafuti",
    "activity_periods": [
      {
        "start_time": "Jul 13 2005 7:10AM",
        "end_time": "Jul 13 2005 8:57AM"
      },
      {
        "start_time": "Jun 20 2017 5:03AM",
        "end_time": "Jun 20 2017 6:55AM"
      },
      {
        "start_time": "Jan 25 2007 9:02AM",
        "end_time": "Jan 25 2007 4:34PM"
      }
    ]
  }]
```


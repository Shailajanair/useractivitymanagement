**PROJECT AIM**

Design and implement a Django application with User and ActivityPeriod models, write  a custom management command
to populate the database with some dummy data, and design an API to serve that data in the json format.

**PACKAGES USED**

asgiref==3.3.1
Django==3.1.6
djangorestframework==3.12.2
pytz==2021.1
sqlparse==0.4.1
names==0.3.0

**END API TO TEST**
http://shailajanair.pythonanywhere.com/user/custom_user/

**SAMPLE RESPONSE**

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
    },
    {
        "id": "PJA459970",
        "real_name": "Mary Smith",
        "timezone": "Pacific/Pohnpei",
        "activity_periods": [
            {
                "start_time": "Jan 19 2006 6:03AM",
                "end_time": "Jan 19 2006 5:32PM"
            },
            {
                "start_time": "Sep 18 2012 7:03AM",
                "end_time": "Sep 18 2012 8:10AM"
            },
            {
                "start_time": "Nov 19 2014 12:37PM",
                "end_time": "Nov 19 2014 5:50PM"
            }
        ]
    },
    {
        "id": "E9D26IKUG",
        "real_name": "Ronald Starkey",
        "timezone": "Asia/Irkutsk",
        "activity_periods": [
            {
                "start_time": "Jul 13 2020 3:22PM",
                "end_time": "Jul 13 2020 4:23PM"
            },
            {
                "start_time": "Apr 20 2019 12:32PM",
                "end_time": "Apr 20 2019 4:57PM"
            },
            {
                "start_time": "Apr 20 2017 8:23AM",
                "end_time": "Apr 20 2017 4:40PM"
            }
        ]
    },
    {
        "id": "Y04GTF4Z5",
        "real_name": "Christopher Willingham",
        "timezone": "America/Tegucigalpa",
        "activity_periods": [
            {
                "start_time": "Apr 18 2019 7:03AM",
                "end_time": "Apr 18 2019 4:52PM"
            },
            {
                "start_time": "May 14 2009 9:41AM",
                "end_time": "May 14 2009 10:53AM"
            },
            {
                "start_time": "Nov 24 2016 7:52AM",
                "end_time": "Nov 24 2016 8:56AM"
            }
        ]
    },
    {
        "id": "Z7VFYDCML",
        "real_name": "Arthur Lynch",
        "timezone": "Europe/Kaliningrad",
        "activity_periods": [
            {
                "start_time": "Nov 7 2003 8:40AM",
                "end_time": "Nov 7 2003 1:58PM"
            },
            {
                "start_time": "Mar 6 2006 7:06AM",
                "end_time": "Mar 6 2006 8:54AM"
            },
            {
                "start_time": "Mar 18 2012 10:11AM",
                "end_time": "Mar 18 2012 4:25PM"
            }
        ]
    },
    {
        "id": "SPMKL506S",
        "real_name": "Dawn Duckett",
        "timezone": "Asia/Kamchatka",
        "activity_periods": [
            {
                "start_time": "Aug 9 2002 5:00AM",
                "end_time": "Aug 9 2002 12:26PM"
            },
            {
                "start_time": "Jul 2 2013 11:07AM",
                "end_time": "Jul 2 2013 4:30PM"
            },
            {
                "start_time": "Apr 8 2003 8:22AM",
                "end_time": "Apr 8 2003 9:57AM"
            }
        ]
    },
    {
        "id": "EAH0RHN9J",
        "real_name": "Blaine Sosa",
        "timezone": "America/Cayenne",
        "activity_periods": [
            {
                "start_time": "Aug 17 2017 7:09AM",
                "end_time": "Aug 17 2017 8:24AM"
            },
            {
                "start_time": "Nov 9 2017 6:05AM",
                "end_time": "Nov 9 2017 6:10PM"
            },
            {
                "start_time": "Mar 11 2004 8:15AM",
                "end_time": "Mar 11 2004 10:44AM"
            }
        ]
    },
    {
        "id": "Y7WH2X4VB",
        "real_name": "Viola Landess",
        "timezone": "America/Belize",
        "activity_periods": [
            {
                "start_time": "Feb 15 2017 12:13PM",
                "end_time": "Feb 15 2017 1:38PM"
            },
            {
                "start_time": "Feb 20 2001 6:39AM",
                "end_time": "Feb 20 2001 1:50PM"
            },
            {
                "start_time": "May 8 2000 12:05PM",
                "end_time": "May 8 2000 2:57PM"
            }
        ]
    },
    {
        "id": "NLB5J5BOR",
        "real_name": "Leonard Duhl",
        "timezone": "America/Guayaquil",
        "activity_periods": [
            {
                "start_time": "Feb 17 2009 7:02AM",
                "end_time": "Feb 17 2009 8:59AM"
            },
            {
                "start_time": "May 15 2015 3:22PM",
                "end_time": "May 15 2015 3:36PM"
            },
            {
                "start_time": "Jul 9 2021 5:22AM",
                "end_time": "Jul 9 2021 5:22AM"
            }
        ]
    }
]

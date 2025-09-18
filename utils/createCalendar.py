import hashlib
from datetime import datetime

import pytz
from icalendar import Calendar, Event, Timezone, TimezoneStandard, TimezoneDaylight
import os
import env
from datatypes.lectureEvent import LectureEvent


def create_uid(title, start, end):
    """Generated hash out of title, start and end time"""
    data = f"{title}{start}{end}"
    return hashlib.md5(data.encode("utf-8")).hexdigest() + env.UID_POSTFIX


def create_ics(events: list[LectureEvent], filename: str = "timetable.ics") -> None:
    """
    Create an ICS calendar file from a list of LectureEvent objects.

    Args:
        events: List of LectureEvent objects.
        filename: Name of the ICS file to generate.
    """
    tz = pytz.timezone(env.TIMEZONE)

    cal = Calendar()
    cal.add("prodid", "-//Uni Timetable//DE")
    cal.add("version", "2.0")

    tz_component = Timezone()
    tz_component.add("tzid", env.TIMEZONE)
    tz_component.add("x-lic-location", env.TIMEZONE)

    # Standard time (CET)
    standard = TimezoneStandard()
    standard.add("tzname", "CET")
    standard.add("tzoffsetfrom", "+0200")
    standard.add("tzoffsetto", "+0100")
    standard.add("dtstart", datetime(1970, 10, 25, 3, 0, 0))
    standard.add("rrule", {"freq": "yearly", "bymonth": 10, "byday": "-1SU"})

    # Daylight time (CEST)
    daylight = TimezoneDaylight()
    daylight.add("tzname", "CEST")
    daylight.add("tzoffsetfrom", "+0100")
    daylight.add("tzoffsetto", "+0200")
    daylight.add("dtstart", datetime(1970, 3, 29, 2, 0, 0))
    daylight.add("rrule", {"freq": "yearly", "bymonth": 3, "byday": "-1SU"})

    tz_component.add_component(standard)
    tz_component.add_component(daylight)

    cal.add_component(tz_component)


    for e in events:
        event = Event()
        event.add("summary", e.title)
        event.add("dtstart", e.start.astimezone(tz))
        event.add("dtend", e.end.astimezone(tz))
        event.add("location", e.location)
        event.add("description", e.description)
        event.add("uid", create_uid(e.title, e.start, e.end))
        cal.add_component(event)

    # Write ICS file in UTF-8
    safe_dir = "output"
    os.makedirs(safe_dir, exist_ok=True)
    safe_filename = os.path.basename(filename)
    full_path = os.path.join(safe_dir, safe_filename)
    with open(full_path, "wb") as f:
        f.write(cal.to_ical())

    print(f"{len(events)} events written to {filename} ✅")
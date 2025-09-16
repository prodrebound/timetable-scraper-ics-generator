import hashlib

import pytz
from icalendar import Calendar, Event
import os
import env
from datatypes.lectureEvent import LectureEvent


def create_uid(title, start, end):
    """Generated hash out of title, start and end time"""
    data = f"{title}{start}{end}"
    return hashlib.md5(data.encode("utf-8")).hexdigest() + env.UID_POSTFIX


def create_ics(events: list[LectureEvent], filename: str = "stundenplan.ics") -> None:
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
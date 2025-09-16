import requests
from bs4 import BeautifulSoup
from dateutil import parser
from datatypes.lectureEvent import LectureEvent
from utils.getLocations import get_location_from_room_description
from utils.specialCases import check_if_module_excluded

def scrape_timetable(url, events=[]):
    """
    Scrape the timetable from the given URL and return a list of LectureEvent objects.
    1. Send a GET request to the URL.
    2. Parse the HTML content using BeautifulSoup.
    3. Find all div elements with the class "week".
    4. For each week div, find all button elements with the class "day-event schedule".
    5. Extract the start and end times, room information, and title from each button.
    6. Create LectureEvent objects and add them to a list, excluding any modules specified in env.EXCLUDE_MODULES.
    7. Return the list of LectureEvent objects.
    8. Handle any potential exceptions during the request or parsing process.
    9. Ensure that the datetime objects are timezone-aware using the specified timezone from env.TIMEZONE.
    10. If room information is available, use get_location_from_room_description to get the location.
    11. If no room information is available, set the location to an empty string.
    12. The description field of LectureEvent can be left empty for now.
    13. Make sure to strip any leading or trailing whitespace from the title and room information.
    14. Return the final list of LectureEvent objects.

    Make sure to adjust the selectors if the HTML structure changes or is different on your timetable site.
    """
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text, "html.parser")

    for week_div in soup.select("div.week"):
        for btn in week_div.select("button.day-event.schedule"):
            start = parser.isoparse(btn["data-start"].split("[")[0])
            end = parser.isoparse(btn["data-end"].split("[")[0])
            room = f"({btn.select_one(".rooms").get_text(strip=True)})" if btn.select_one(".rooms") else ""
            title = f"{btn.select_one(".text").get_text(strip=True)}"
            title_with_room = f"{title} {room}"
            location = get_location_from_room_description(room.split("/")[0])
            if not check_if_module_excluded(title):
                events.append(LectureEvent(title_with_room, start, end, location, description=""))
    return events
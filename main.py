import env
from utils.createCalendar import create_ics
from utils.scraper import scrape_timetable


events = scrape_timetable(env.TIMETABLE_URL)

if env.CHECK_ADDITIONAL_TIMETABLES:
    for url in env.ADDITIONAL_TIMETABLE_URLS:
        events = scrape_timetable(url, events)
    events.sort(key=lambda x: x.start)

create_ics(events, env.ICS_FILE_DESTINATION)

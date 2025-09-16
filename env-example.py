TIMEZONE = "Europe/Berlin" # Timezone indentifier for the events (e.g. "Europe/Berlin", "America/New_York", https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
CHECK_ADDITIONAL_TIMETABLES = False # Whether to check additional timetable URLs
UID_POSTFIX = "@university.org"
TIMETABLE_URL = ""
ADDITIONAL_TIMETABLE_URLS = [

] # Additional timetable URLs to check (if CHECK_ADDITIONAL_TIMETABLES is True)
EXCLUDE_MODULES = [

]
ICS_FILE_DESTINATION = "timetable.ics" # Path to save the .ics file
ROOM_TO_ADRESS = {
} # Mapping from room names (e.g. AB-CE-2 -> I can derive this to a certain address) to addresses for geolocation
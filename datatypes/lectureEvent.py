from dataclasses import dataclass
from datetime import datetime


@dataclass
class LectureEvent:
    title: str
    start: datetime
    end: datetime
    location: str = ""
    description: str = ""
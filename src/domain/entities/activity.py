# Façam validação dos atributos
from typing import List

from src.domain.entities.schedule import Schedule
from src.domain.entities.speaker import Speaker


class Activity:
    title: str
    code: str
    description: str
    activityType: str
    speakers: List[Speaker]
    schedule: List[Schedule]

    def __init__(self, title, code, description, activityType, speakers, schedule):

        self.title = title
        self.code = code
        self.description = description
        self.activityType = activityType
        self.speakers = speakers
        self.schedule = schedule

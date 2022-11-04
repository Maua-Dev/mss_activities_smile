from typing import List

from src.domain.entities.schedule import Schedule
from src.domain.entities.speaker import Speaker
from src.helpers.domain_errors import EntityError


class Activity:
    title: str
    code: str
    description: str
    activityType: str
    speakers: List[Speaker]
    schedule: List[Schedule]

    def __init__(self, title, code, description, activityType, speakers, schedule):
        if not Activity.validate_title(title):
            raise EntityError('title')
        self.title = title

        if not Activity.validate_code(code):
            raise EntityError('code')
        self.code = code

        if not Activity.validate_description(description):
            raise EntityError('description')
        self.description = description

        if not Activity.validate_activityType(activityType):
            raise EntityError('activityType')
        self.activityType = activityType

        if not Activity.validate_speakers(speakers):
            raise EntityError('speakers')
        self.speakers = speakers

        if not Activity.validate_schedule(schedule):
            raise EntityError('schedule')
        self.schedule = schedule

    @staticmethod
    def validate_title(title: str) -> bool:
    
        if title == None:
            return False

        if type(title) != str:
            return False

        return True

    @staticmethod
    def validate_code(code: str) -> bool:
   
        if code == None:
            return False

        if type(code) != str:
            return False

        if "Código" not in code:
            return False

        return True
       
    @staticmethod
    def validate_description(description: str) -> bool:
    
        if description == None:
            return False

        if type(description) != str:
            return False

        return True

    @staticmethod
    def validate_activityType(activityType: str) -> bool:
   
        if activityType == None:
            return False

        if type(activityType) != str:
            return False

        return True

    @staticmethod
    def validate_speakers(speakers: list) -> bool:
    
        if len(speakers) == 0:
            return False

        if type(speakers) != list:
            return False

        return True

    @staticmethod
    def validate_schedule(schedule: list) -> bool:
        if len(schedule) == 0:
            return False

        if type(schedule) != list:
            return False

        return True
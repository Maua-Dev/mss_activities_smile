from src.domain.entities.activity import Activity

from typing import List

from src.domain.entities.schedule import Schedule
from src.domain.entities.speaker import Speaker


class SpeakerViewModel:
    speakers: List[Speaker]
    name: str
    bio: str
    company: str

    def __init__(self, speakers: List[Speaker]) -> None:
        self.speakers = speakers

    def to_dict(self):
        return [{
            'name': speaker.name,
            'bio': speaker.bio,
            'company': speaker.company,
        } for speaker in self.speakers]


class ScheduleViewModel:
    schedules: List[Schedule]
    initialDate: str
    maxParticipants: int
    finalDate: str
    location: str
    remoteRoomUrl: str
    acceptSubscriptionUntilDate: bool

    # enrolledUsers

    def __init__(self, schedules: List[Schedule]) -> None:
        self.schedules = schedules

    def to_dict(self):
        return [{
            'date': schedule.initialDate,
            'totalParticipants': schedule.maxParticipants,
            'duration': schedule.finalDate,
            'location': schedule.location,
            'link': schedule.remoteRoomUrl,
            'acceptSubscription': schedule.acceptSubscription
            # 'enrolledUsers': self.enrolledUsers
        } for schedule in self.schedules]


class ActivityViewModel:
    title: str
    code: str
    description: str
    activity_type: str
    speakers: SpeakerViewModel
    schedule: ScheduleViewModel

    def __init__(self, data: Activity):
        self.title = data.title
        self.code = data.code
        self.description = data.description
        self.activity_type = data.activity_type
        self.speakers = SpeakerViewModel(data.speakers)
        self.schedule = ScheduleViewModel(data.schedule)

    def to_dict(self):
        return {
            'activityCode': self.code,
            'type': self.activity_type,
            'title': self.title,
            'description': self.description,
            'schedule': self.schedule.to_dict(),
            'speakers': self.speakers.to_dict()
        }


class GetAllActivitiesViewmodel:
    activities: List[ActivityViewModel] = []

    def __init__(self, data: List[Activity]):
        self.activities = [ActivityViewModel(activity) for activity in data]

    def to_dict(self):
        return [activity.to_dict() for activity in self.activities]

import datetime

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
    initialDate: datetime.datetime
    finalDate: datetime.datetime
    maxParticipants: int
    duration: datetime.timedelta
    location: str
    remoteRoomUrl: str
    acceptSubscriptionUntilDate: bool

    # enrolledUsers

    def __init__(self, schedules: List[Schedule]) -> None:
        self.schedules = schedules

    def to_dict(self):
        return [{
            'date': datetime.datetime.timestamp(schedule.initialDate),
            'totalParticipants': schedule.maxParticipants,
            'duration': schedule.duration.total_seconds() * 1000
                        or (schedule.finalDate - schedule.initialDate).total_seconds() * 1000,
            'location': schedule.location,
            'link': schedule.remoteRoomUrl,
            'acceptSubscription': schedule.acceptSubscription
            # 'enrolledUsers': self.enrolledUsers
        } for schedule in self.schedules]


class ActivityViewModel:
    title: str
    code: str
    description: str
    activityType: str
    speakers: SpeakerViewModel
    schedule: ScheduleViewModel

    def __init__(self, data: Activity):
        self.title = data.title
        self.code = data.code
        self.description = data.description
        self.activityType = data.activityType
        self.speakers = SpeakerViewModel(data.speakers)
        self.schedule = ScheduleViewModel(data.schedule)

    def to_dict(self):
        return {
            'activityCode': self.code,
            'type': self.activityType,
            'title': self.title,
            'description': self.description,
            'schedule': self.schedule.to_dict(),
            'speakers': self.speakers.to_dict()
        }


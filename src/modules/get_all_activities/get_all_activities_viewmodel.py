from src.domain.entities.activity import Activity

from typing import List


class ScheduleViewModel:
    initialDate: str
    maxParticipants: int
    finalDate: str
    location: str
    remoteRoomUrl: str
    acceptSubscriptionUntilDate: bool
    # enrolledUsers

    def __init__(self, data: Activity) -> None:
        self.initialDate = data.initialDate
        self.maxParticipants = data.maxParticipants
        self.finalDate = data.finalDate
        self.location = data.location
        self.remoteRoomUrl = data.remoteRoomUrl
        self.acceptSubscriptionUntilDate = data.acceptSubscriptionUntilDate

    def to_dict(self):
        return {
            'date': self.initialDate,
            'totalParticipants': self.maxParticipants,
            'duration': self.finalDate,
            'location': self.location,
            'link': self.remoteRoomUrl,
            'acceptSubscription': self.acceptSubscriptionUntilDate
            # 'enrolledUsers': self.enrolledUsers
        }


class ActivityViewModel:
    title: str
    type: str
    code: str
    description: str
    activityType: str
    speakers: str
    schedule: ScheduleViewModel

    def __init__(self, data: Activity):

        self.title = data.title
        self.type = data.type
        self.code = data.code
        self.description = data.description
        self.activityType = data.activityType
        self.speakers = data.speakers
        self.schedule = ScheduleViewModel(data)

    def to_dict(self):
        return {
            'activityCode': self.code,
            'type': self.type,
            'title': self.title,
            'description': self.description,
            'schedule': self.schedule.to_dict(),
            'speakers': self.speakers
        }


class GetAllActivitiesViewmodel:
    activities: List[ActivityViewModel] = []

    def __init__(self, data: List[Activity]):
        self.activities = [ActivityViewModel(activity) for activity in data]

    def to_dict(self):
        return [activity.to_dict() for activity in self.activities]


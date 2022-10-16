from typing import List
from src.domain.entities.activity import Activity


class GetActivityViewModel:
    title: str
    type: str
    code: str
    description: str
    initialDate: str
    finalDate: str
    activityType: str
    speakers: str
    acceptSubscriptionUntilDate: bool
    location: str
    remoteRoomUrl: str
    acceptSubscription: bool
    maxParticipants: int

    def __init__(self, activity: Activity):
        self.title = activity.title
        self.type = activity.type
        self.code = activity.code
        self.description = activity.description
        self.initialDate = activity.initialDate
        self.finalDate = activity.finalDate
        self.activityType = activity.activityType
        self.speakers = activity.speakers
        self.acceptSubscriptionUntilDate = activity.acceptSubscriptionUntilDate
        self.location = activity.location
        self.remoteRoomUrl = activity.remoteRoomUrl
        self.acceptSubscription = activity.acceptSubscription
        self.maxParticipants = activity.maxParticipants

    def to_dict(self) -> dict:
        return {

            "title": self.title,
            "type": self.type,
            "code": self.code,
            "description": self.description,
            "initialDate": self.isoformat,
            "finalDate": self.isoformat(),
            "activityType": self.activityType,
            "speakers": self.speakers,
            "acceptSubscriptionUntilDate": self.acceptSubscriptionUntilDate,
            "location": self.location,
            "remoteRoomUrl": self.remoteRoomUrl,
            "acceptSubscription": self.acceptSubscription,
            "maxParticipants": self.maxParticipants

        }

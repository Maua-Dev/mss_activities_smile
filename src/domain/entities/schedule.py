# Façam validação dos atributos
import datetime


class Schedule:
    initialDate: datetime.datetime
    finalDate: datetime.datetime
    duration: datetime.time
    maxParticipants: int
    location: str
    remoteRoomUrl: str
    acceptSubscription: bool
    acceptSubscriptionUntilDate: bool

    def __init__(self,
                 initialDate,
                 finalDate,
                 duration,
                 maxParticipants,
                 location,
                 remoteRoomUrl,
                 acceptSubscription,
                 acceptSubscriptionUntilDate
                 ):
        self.initialDate = initialDate
        self.finalDate = finalDate or initialDate + duration
        self.duration = duration or finalDate - initialDate
        self.maxParticipants = maxParticipants
        self.location = location
        self.remoteRoomUrl = remoteRoomUrl
        self.acceptSubscription = acceptSubscription
        self.acceptSubscriptionUntilDate = acceptSubscriptionUntilDate

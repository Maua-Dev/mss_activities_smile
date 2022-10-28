# Façam validação dos atributos

class Schedule:
    initialDate: str
    finalDate: str
    maxParticipants: int
    location: str
    remoteRoomUrl: str
    acceptSubscription: bool
    acceptSubscriptionUntilDate: bool

    def __init__(self,
                 initialDate,
                 finalDate,
                 maxParticipants,
                 location,
                 remoteRoomUrl,
                 acceptSubscription,
                 acceptSubscriptionUntilDate
                 ):
        self.initialDate = initialDate
        self.finalDate = finalDate
        self.maxParticipants = maxParticipants
        self.location = location
        self.remoteRoomUrl = remoteRoomUrl
        self.acceptSubscription = acceptSubscription
        self.acceptSubscriptionUntilDate = acceptSubscriptionUntilDate

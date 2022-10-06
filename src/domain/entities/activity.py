
# Façam validação dos atributos

class Activity:
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
    #devem ser declarados como string ou um int? 
    maxParticipants: int




    def __init__(self, title, type, code, description, initialDate, 
                finalDate, activityType, speakers, acceptSubscriptionUntilDate, 
                location, remoteRoomUrl, acceptSubscription, maxParticipants):

        self.title = title
        self.type = type
        self.code = code
        self.description = description
        self.initialDate = initialDate
        self.finalDate = finalDate
        self.activityType = activityType
        self.speakers = speakers
        self.acceptSubscriptionUntilDate = acceptSubscriptionUntilDate
        self.location = location
        self.remoteRoomUrl = remoteRoomUrl
        self.acceptSubscription = acceptSubscription
        self.maxParticipants = maxParticipants





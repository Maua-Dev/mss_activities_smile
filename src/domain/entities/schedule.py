from datetime import datetime, timedelta


class Schedule:
    initialDate: datetime.datetime
    finalDate: datetime.datetime
    duration: datetime.timedelta
    maxParticipants: int
    location: str
    remoteRoomUrl: str
    acceptSubscription: bool
    acceptSubscriptionUntilDate: datetime.datetime

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
        

        @staticmethod
        def validate_time(finalDate: datetime, 
                        initialDate: datetime, 
                        duration: datetime) -> bool:

            #finalDate validation
            if finalDate == None:
                return False

            if not isinstance(finalDate, datetime):
                return False

            #initialDate validation
            if initialDate == None:
                return False

            if not isinstance(initialDate, datetime):
                return False            

            #duration validation:
            if duration == None:
                return False

            if not isinstance(duration, timedelta):
                return False 
            
            if (initialDate >= finalDate) or (duration != (finalDate - initialDate)):
                return False

            return True

        @staticmethod
        def validate_maxParticipants(maxParticipants: int) -> bool:
        
            if maxParticipants == None:
                return False

            if maxParticipants <= 0:
                return False

            if type(maxParticipants) != int:
                return False

            return True

        @staticmethod
        def validate_location(location: str)->bool:
        
            if location == None:
                return False

            if type(location) != str:
                return False

            return True

        @staticmethod
        def validate_remoteRoomUrl(remoteRoomUrl: str) -> bool:
        
            if remoteRoomUrl == None:
                return False

            if type(remoteRoomUrl) != str:
                return False

            return True

        @staticmethod
        def validate_acceptSubscription(acceptSubscription: bool) -> bool:
        
            if acceptSubscription is False:
                return False

            if type(acceptSubscription) != bool:
                return False   

            return True
            
        @staticmethod
        def validate_acceptSubscriptionUntilDate(acceptSubscriptionUntilDate: datetime) -> bool:
        
            if acceptSubscriptionUntilDate is None:
                return False

            if not isinstance(acceptSubscriptionUntilDate, datetime):
                return False

            return True
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
        if not Schedule.validate_initialDate(initialDate):
            raise Schedule('initialDate')
        self.initialDate = initialDate

        if not Schedule.finalDate:
            raise Schedule('finalDate')
        if not Schedule.duration:
            raise('duration')
        if not Schedule.initialDate:
            raise('initialDate')
        self.finalDate = finalDate or initialDate + duration 
        self.duration = duration or finalDate - initialDate

        #confirmar com o Rocha
        self.maxParticipants = maxParticipants
        if not Schedule.validate_location(location):
            raise Schedule('schedule')
        self.location = location

        if not Schedule.validate_remoteRoomUrl(remoteRoomUrl):
            raise Schedule('remoteRoomUrl')
        self.remoteRoomUrl = remoteRoomUrl

        if not Schedule.acceptSubscription(acceptSubscription):
            raise Schedule('acceptSubscription')
        self.acceptSubscription = acceptSubscription

        if not Schedule.acceptSubscriptionUntilDate(acceptSubscriptionUntilDate):
            raise Schedule('acceptSubscriptionUntilDate')
        self.acceptSubscriptionUntilDate = acceptSubscriptionUntilDate
        

        @staticmethod
        def validate_time(finalDate: datetime, 
                        initialDate: datetime, 
                        duration: datetime) -> bool:

            # finalDate validation
            if finalDate is None or duration is None:
                return False

            if not isinstance(finalDate, datetime):
                return False

            #initialDate validation
            if initialDate is None:
                return False

            if not isinstance(initialDate, datetime):
                return False           

            if not isinstance(duration, timedelta):
                return False 
            
            if (initialDate >= finalDate) or (duration != (finalDate - initialDate)):
                return False

            return True
        # Confirmar com o Rocha
        @staticmethod
        def validate_maxParticipants(maxParticipants: int) -> bool:
        
            if maxParticipants is None:
                return False

            if maxParticipants <= 0:
                return False

            if type(maxParticipants) != int:
                return False

            return True

        @staticmethod
        def validate_location(location: str)->bool:
        
            if location is None:
                return False

            if type(location) != str:
                return False

            return True

        @staticmethod
        def validate_remoteRoomUrl(remoteRoomUrl: str) -> bool:
        
            if remoteRoomUrl is None:
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
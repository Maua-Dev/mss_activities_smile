import datetime
from typing import List

from src.domain.entities.activity import Activity
from src.domain.entities.schedule import Schedule
from src.domain.entities.speaker import Speaker
from src.domain.repositories.activity_repository_interface import IActivityRepository


class ActivityRepositoryMock(IActivityRepository):
    activities: List[Activity]

    def __init__(self):
        self.activities = [
            Activity(title='Atividade 1', code='Código 1', description='Descrição 1', activityType='Tipo 1',
                     speakers=[
                         Speaker(
                             name='Nome Sobrenome 1',
                             bio='bla bla bla',
                             company='Dev Community Mauá'
                         )
                     ],
                     schedule=[
                         Schedule(
                             initialDate=datetime.datetime(year=2022, month=9, day=20, hour=10,
                                                           minute=00, tzinfo=pytz.timezone('Etc/UTC')),
                             finalDate=datetime.datetime(year=2022, month=9, day=20, hour=11,
                                                         minute=00, tzinfo=pytz.timezone('Etc/UTC')),
                             maxParticipants=100,
                             location='H201',
                             remoteRoomUrl='https://zoom.com/etc/1/',
                             acceptSubscription=True,
                             acceptSubscriptionUntilDate=datetime.datetime(year=2022, month=9, day=20, hour=11,
                                                                           minute=00, tzinfo=pytz.timezone('Etc/UTC')),
                             duration=None
                         )
                     ]
                     ),
            Activity(title='Atividade 2', code='Código 2', description='Descrição 2', activityType='Tipo 2',
                     speakers=[
                         Speaker(
                             name='Nome Sobrenome 2',
                             bio='bla bla bla',
                             company='Dev Community Mauá'
                         )
                     ],
                     schedule=[
                         Schedule(
                             initialDate=datetime.datetime(year=2022, month=9, day=20, hour=10,
                                                           minute=00, tzinfo=pytz.timezone('Etc/UTC')),
                             finalDate=datetime.datetime(year=2022, month=9, day=20, hour=11,
                                                         minute=00, tzinfo=pytz.timezone('Etc/UTC')),
                             maxParticipants=100,
                             location='H201',
                             remoteRoomUrl='https://zoom.com/etc/1/',
                             acceptSubscription=True,
                             acceptSubscriptionUntilDate=datetime.datetime(year=2022, month=9, day=20, hour=11,
                                                                           minute=00, tzinfo=pytz.timezone('Etc/UTC')),
                             duration=None
                         )
                     ]
                     ),

            Activity(title='Atividade 3', code='Código 3', description='Descrição 3', activityType='Tipo 3',
                     speakers=[
                         Speaker(
                             name='Nome Sobrenome 3',
                             bio='bla bla bla',
                             company='Dev Community Mauá'
                         )
                     ],
                     schedule=[
                         Schedule(
                             initialDate=datetime.datetime(year=2022, month=9, day=20, hour=10,
                                                           minute=00, tzinfo=pytz.timezone('Etc/UTC')),
                             finalDate=datetime.datetime(year=2022, month=9, day=20, hour=11,
                                                         minute=00, tzinfo=pytz.timezone('Etc/UTC')),
                             maxParticipants=100,
                             location='H201',
                             remoteRoomUrl='https://zoom.com/etc/1/',
                             acceptSubscription=True,
                             acceptSubscriptionUntilDate=datetime.datetime(year=2022, month=9, day=20, hour=11,
                                                                           minute=00, tzinfo=pytz.timezone('Etc/UTC')),
                             duration=None
                         )
                     ]
                     ),
            Activity(title='Atividade 4', code='Código 4', description='Descrição 4', activityType='Tipo 4',
                     speakers=[
                         Speaker(
                             name='Nome Sobrenome 2',
                             bio='bla bla bla',
                             company='Dev Community Mauá'
                         )
                     ],
                     schedule=[
                         Schedule(
                             initialDate=datetime.datetime(year=2022, month=9, day=20, hour=10,
                                                           minute=00, tzinfo=pytz.timezone('Etc/UTC')),
                             finalDate=datetime.datetime(year=2022, month=9, day=20, hour=11,
                                                         minute=00, tzinfo=pytz.timezone('Etc/UTC')),
                             maxParticipants=100,
                             location='H201',
                             remoteRoomUrl='https://zoom.com/etc/1/',
                             acceptSubscription=True,
                             acceptSubscriptionUntilDate=datetime.datetime(year=2022, month=9, day=20, hour=11,
                                                                           minute=00, tzinfo=pytz.timezone('Etc/UTC')),
                             duration=None
                         )
                     ]
                     ),
        ]

    def get_all_activities(self) -> List[Activity]:
        return self.activities

    def get_activity_by_code(self, activity_code: str) -> Activity:
        for activity in self.activities:
            if activity.code == activity_code:
                return activity

        return None

    def delete_activity(self, code: str) -> bool:
        activities_aux = []

        for activity in self.activities:
            if activity.code != code:
                activities_aux.append(activity)
        self.activities = activities_aux
        return True

    def create_activity(self, activity: Activity) -> bool:
        self.activities.append(activity)
        return True


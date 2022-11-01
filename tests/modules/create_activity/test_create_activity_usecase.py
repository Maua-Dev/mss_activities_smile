import datetime

from src.domain.entities.activity import Activity
from src.domain.entities.schedule import Schedule
from src.domain.entities.speaker import Speaker
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.create_activity.create_activity_usecase import CreateActivityUsecase


class Test_CreateActivityUsecase:

    def test_create_activity_usecase(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo)
        len_before = len(repo.activities)
        res = usecase(
            activity=Activity(title='Atividade 5', code='Código 5', description='Descrição 5', activityType='Tipo 5',
                              speakers=[
                                  Speaker(
                                      name='Nome Sobrenome 5',
                                      bio='bla bla bla',
                                      company='Dev Community Mauá'
                                  )
                              ],
                              schedule=[
                                  Schedule(
                                      initialDate=datetime.datetime(year=2022, month=9, day=20, hour=10, minute=00),
                                      finalDate=None,
                                      maxParticipants=100,
                                      location='H201',
                                      remoteRoomUrl='https://zoom.com/etc/1/',
                                      acceptSubscription=True,
                                      acceptSubscriptionUntilDate='2021-01-02',
                                      duration=datetime.timedelta(minutes=60)
                                  )
                              ]
                              ), )
        len_after = len(repo.activities)
        assert repo.activities[-1].code == "Código 5"
        assert res
        assert len_before == len_after - 1

import datetime
from src.domain.entities.activity import Activity
from src.domain.entities.schedule import Schedule
from src.domain.entities.speaker import Speaker

from src.helpers.http_models import HttpRequest
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.update_activity.update_activity_controller import UpdateActivityController
from src.modules.update_activity.update_activity_usecase import UpdateActivityUsecase

class Test_UpdateActivityController:

    def test_update_activity_controller_code_only(self):
       repo = ActivityRepositoryMock()
       usecase = UpdateActivityUsecase(repo=repo)
       controller = UpdateActivityController(usecase=usecase)
       request = HttpRequest(body={
              "code": "Código 1",
       })
       response = controller(request=request)

       expected = Activity(
              title="Atividade 1",
              code="Código 1",
              description="Descrição 1",
              activityType="Tipo 1",
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
       )

       assert response.status_code == 200
       assert response.body['title'] == expected.title
       assert response.body['code']== expected.code
       assert response.body['description'] == expected.description
       assert response.body['activityType'] == expected.activityType
       assert response.body['speakers'] == expected.speakers
       assert response.body['schedule'] == expected.schedule
       assert response.body['message'] == "User was updated successfully"
        
    def test_update_activity_controller_ra_title(self):
       repo = ActivityRepositoryMock()
       usecase = UpdateActivityUsecase(repo=repo)
       controller = UpdateActivityController(usecase=usecase)
       request = HttpRequest(body={
            "code": "Código 1",
            "new_title": "Atividade Nova",
       })
       response = controller(request=request)

       expected = Activity(
              title="Atividade Nova",
              code="Código 1",
              description="Descrição 1",
              activityType="Tipo 1",
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
       )

       assert response.status_code == 200
       assert response.body['title'] == expected.title
       assert response.body['code']== expected.code
       assert response.body['description'] == expected.description
       assert response.body['activityType'] == expected.activityType
       assert response.body['speakers'] == expected.speakers
       assert response.body['schedule'] == expected.schedule
       assert response.body['message'] == "User was updated successfully"

    def test_update_activity_controller_ra_description(self):
       repo = ActivityRepositoryMock()
       usecase = UpdateActivityUsecase(repo=repo)
       controller = UpdateActivityController(usecase=usecase)
       request = HttpRequest(body={
            "code": "Código 1",
            "new_description": "Descrição Nova",
       })
       response = controller(request=request)

       expected = Activity(
              title="Atividade Nova",
              code="Código 1",
              description="Descrição Nova",
              activityType="Tipo 1",
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
       )

       assert response.status_code == 200
       assert response.body['title'] == expected.title
       assert response.body['code']== expected.code
       assert response.body['description'] == expected.description
       assert response.body['activityType'] == expected.activityType
       assert response.body['speakers'] == expected.speakers
       assert response.body['schedule'] == expected.schedule
       assert response.body['message'] == "User was updated successfully"

    def test_update_activity_controller_ra_title_description(self):
       repo = ActivityRepositoryMock()
       usecase = UpdateActivityUsecase(repo=repo)
       controller = UpdateActivityController(usecase=usecase)
       request = HttpRequest(body={
            "code": "Código 1",
            "title": "Atividade Velha",
            "new_description": "Descrição Velha",
       })
       response = controller(request=request)

       expected = Activity(
              title="Atividade Velha",
              code="Código 1",
              description="Descrição Velha",
              activityType="Tipo 1",
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
       )

       assert response.status_code == 200
       assert response.body['title'] == expected.title
       assert response.body['code']== expected.code
       assert response.body['description'] == expected.description
       assert response.body['activityType'] == expected.activityType
       assert response.body['speakers'] == expected.speakers
       assert response.body['schedule'] == expected.schedule
       assert response.body['message'] == "User was updated successfully"

    def test_update_activity_controller_no_items_found(self):
       repo = ActivityRepositoryMock()
       usecase = UpdateActivityUsecase(repo=repo)
       controller = UpdateActivityController(usecase=usecase)

       request = HttpRequest(body={
            "code": "Código 1",
       })

       response = controller(request=request)

       assert response.body == "No items found for ra"
       assert response.status_code == 404

    def test_update_activity_controller_bad_request(self):
       repo = ActivityRepositoryMock()
       usecase = UpdateActivityUsecase(repo=repo)
       controller = UpdateActivityController(usecase=usecase)

       request = HttpRequest(body={
       })

       response = controller(request=request)

       assert response.status_code == 400
       assert response.body == "Field ra is missing"

    def test_update_activity_controller_bad_request_invalid_code(self):
       repo = ActivityRepositoryMock()
       usecase = UpdateActivityUsecase(repo=repo)
       controller = UpdateActivityController(usecase=usecase)

       request = HttpRequest(body={
            "code": "Código Inválido",
       })

       response = controller(request=request)

       assert response.status_code == 400
       assert response.body == "Field code is not valid"

import datetime

from src.helpers.http_models import HttpRequest
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.create_activity.create_activity_controller import CreateActivityController
from src.modules.create_activity.create_activity_usecase import CreateActivityUsecase


class Test_CreateActivityController:
    request_body: dict
    request_body = {
        'title': 'Atividade 5',
        'activityCode': 'Código 5',
        'description': 'Descrição 5',
        'type': 'Tipo 5',
        'speakers': [
            {
                'name': 'Nome Sobrenome 5',
                'bio': 'bla bla bla',
                'company': 'Dev Community Mauá'
            }
        ],
        'schedule': [
            {
                'initialDate': datetime.datetime(year=2022, month=9, day=20, hour=10, minute=00),
                'finalDate': datetime.datetime(year=2022, month=9, day=20, hour=11, minute=00),
                'totalParticipants': 100,
                'location': 'H201',
                'link': 'https://zoom.com/etc/1/',
                'acceptSubscription': True,
                'acceptSubscriptionUntilDate': datetime.datetime(year=2022, month=9, day=20, hour=11, minute=00),
                'duration': datetime.timedelta(minutes=60)
            }]
    }

    def test_create_activity(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo)
        controller = CreateActivityController(usecase)

        httpRequest = HttpRequest(body=self.request_body)

        httpResponse = controller(httpRequest)

        assert httpResponse.status_code == 201

    def test_create_activity_missing_field(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo)
        controller = CreateActivityController(usecase)

        httpRequest = HttpRequest(
            body={
                'activityCode': 'Código X',
                'schedule': [
                    {'link': ''}
                ]
            })

        httpResponse = controller(httpRequest)

        assert httpResponse.status_code == 400
        assert httpResponse.body == "initialDate is required"

    def test_create_activity_empty_body(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo)
        controller = CreateActivityController(usecase)

        httpRequest = HttpRequest(body={})

        httpResponse = controller(httpRequest)

        assert httpResponse.status_code == 400
        assert httpResponse.body == "activityCode is required"

    def test_create_activity_missing_schedule(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo)
        controller = CreateActivityController(usecase)

        httpRequest = HttpRequest(body={'activityCode': 'Código X'})

        httpResponse = controller(httpRequest)

        assert httpResponse.status_code == 400
        assert httpResponse.body == "schedule is required"

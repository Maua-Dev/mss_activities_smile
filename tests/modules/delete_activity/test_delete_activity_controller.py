from src.helpers.http_models import HttpRequest
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.delete_activity.delete_activity_controller import DeleteActivityController
from src.modules.delete_activity.delete_activity_usecase import DeleteActivityUsecase


class Test_GetActivityByCodeController:
    def test_get_activity(self):
        repo = ActivityRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)

        httpRequest = HttpRequest(body={
            "title": "Atividade 1",
            "type": "Tipo 1",
            "code": "Código 1",
            "description": "Descrição 1",
            "initialDate": "2021-01-01",
            "finalDate": "2021-01-02",
            "activityType": "Palestra",
            "speakers": "Nome Sobrenome 1",
            "acceptSubscriptionUntilDate": True,
            "location": "H201",
            "remoteRoomUrl": "https://zoom.com/etc/1/",
            "acceptSubscription": True,
            "maxParticipants": "40"
        })

        httpResponse = controller(httpRequest)

        assert httpResponse.status_code == 200

    def test_delete_activity_missing_fields(self):
        repo = ActivityRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)

        httpRequest = HttpRequest(body={
            "title": "Atividade 1",
            "type": "Tipo 1",
            "description": "Descrição 1",
            "initialDate": "2021-01-01",
            "finalDate": "2021-01-02",
            "activityType": "Palestra",
            "speakers": "Nome Sobrenome 1",
            "acceptSubscriptionUntilDate": True,
            "location": "H201",
            "remoteRoomUrl": "https://zoom.com/etc/1/",
            "acceptSubscription": True,
            "maxParticipants": "40"
        })

        httpResponse = controller(httpRequest)

        assert httpResponse.status_code == 400
        assert httpResponse.body == "Bad Request: code is required"

        httpRequest = HttpRequest(body={
            "title": "Atividade 1",
            "type": "Tipo 1",
            "description": "Descrição 1",
            "finalDate": "2021-01-02",
            "activityType": "Palestra",
            "speakers": "Nome Sobrenome 1",
            "acceptSubscriptionUntilDate": True,
            "location": "H201",
            "remoteRoomUrl": "https://zoom.com/etc/1/",
            "acceptSubscription": True,
            "maxParticipants": "40"
        })
        httpResponse = controller(httpRequest)

        assert httpResponse.status_code == 400
        assert httpResponse.body == "Bad Request: Initial Date is required"


#Completar conforme errors.py for desenvolvido


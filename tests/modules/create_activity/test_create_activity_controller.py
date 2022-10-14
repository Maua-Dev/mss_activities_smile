from src.helpers.http_models import HttpRequest
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.create_activity.create_activity_controller import CreateActivityController
from src.modules.create_activity.create_activity_usecase import CreateActivityUsecase


class Test_GetActivityByCodeController:

    def test_create_activity(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo)
        controller = CreateActivityController(usecase)

        httpRequest = HttpRequest(body={
                                        "title": "Atividade 4",
                                        "type": "Tipo 4",
                                        "code": "Código 4",
                                        "description": "Descrição 4",
                                        "initialDate": "2021-01-01",
                                        "finalDate": "2021-01-02"
                                        })

        httpResponse = controller(httpRequest)
        assert httpResponse.status_code == 201

    def test_create_activity_missing_fields(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo)
        controller = CreateActivityController(usecase)

        httpRequest = HttpRequest(body={
            "title": "Atividade 4",
            "type": "Tipo 4",
            "description": "Descrição 4",
            "initialDate": "2021-01-01",
            "finalDate": "2021-01-02"
        })

        httpResponse = controller(httpRequest)

        assert httpResponse.status_code == 400
        assert httpResponse.body == "code is required"

        httpRequest = HttpRequest(body={
            "title": "Atividade 4",
            "type": "Tipo 4",
            "code": "Código 4",
            "description": "Descrição 4",
            "finalDate": "2021-01-02"
        })

        httpResponse = controller(httpRequest)

        assert httpResponse.status_code == 400
        assert httpResponse.body == "initialDate is required"

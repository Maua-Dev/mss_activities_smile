from src.helpers.http_models import HttpRequest
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.delete_activity.delete_activity_usecase import DeleteActivityUsecase
from src.modules.delete_activity.delete_activity_controller import DeleteActivityController


class Test_DeleteActivityController:
    def test_delete_activity(self):
        repo = ActivityRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)

        httpRequest = HttpRequest(body={
            "code": "Código 1",
        })

        httpResponse = controller(httpRequest)

        assert httpResponse.status_code == 200

    def test_delete_activity_missing_field(self):
        repo = ActivityRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)

        httpRequest = HttpRequest(body={
            "code": ""
        })

        httpResponse = controller(httpRequest)
        # print(f"httpResponse.body: {httpResponse.body}")
        assert httpResponse.status_code == 400
        assert httpResponse.body == "code is required"
    def test_delete_activity_empty_body(self):
        repo = ActivityRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)

        httpRequest = HttpRequest(body={

        })

        httpResponse = controller(httpRequest)
        # print(f"httpResponse.body: {httpResponse.body}")
        assert httpResponse.status_code == 400
        assert httpResponse.body == "code is required"



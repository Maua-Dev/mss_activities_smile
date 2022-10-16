from src.helpers.http_models import HttpRequest
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.get_activity_by_code.get_activity_by_code_controller import GetActivityByCodeController
from src.modules.get_activity_by_code.get_activity_by_code_usecase import GetActivityByCodeUsecase, ACTIVITY_NOT_FOUND


class Test_GetActivityByCodeController:

    def test_get_activity(self):
        repo = ActivityRepositoryMock()
        usecase = GetActivityByCodeUsecase(repo)
        controller = GetActivityByCodeController(usecase)

        httpRequest = HttpRequest(query_params={"code": "Código 1"})

        httpResponse = controller(httpRequest)

        assert httpResponse.status_code == 200
        assert httpResponse.body == repo.activities[0].__dict__




    def test_get_activity_not_found(self):
        repo = ActivityRepositoryMock()
        usecase = GetActivityByCodeUsecase(repo)
        controller = GetActivityByCodeController(usecase)

        httpRequest = HttpRequest(query_params={"code": "Código 4"})

        httpResponse = controller(httpRequest)

        assert httpResponse.status_code == 404
        assert httpResponse.body == {"message": "Activity with code Código 4 was not found"}


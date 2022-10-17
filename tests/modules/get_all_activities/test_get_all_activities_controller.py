from src.helpers.http_models import HttpRequest
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.get_all_activities.get_all_activities_controller import GetAllActivitiesController
from src.modules.get_all_activities.get_all_activities_usecase import GetAllActivitiesUsecase


class Test_GetAllActivitiesController:

    def test_get_activity(self):
        repo = ActivityRepositoryMock()
        usecase = GetAllActivitiesUsecase(repo)
        controller = GetAllActivitiesController(usecase)

        httpRequest = HttpRequest(query_params={"code": "Código 1"})

        httpResponse = controller(httpRequest)

        assert httpResponse.status_code == 200
        assert httpResponse.body == repo.activities[0].__dict__


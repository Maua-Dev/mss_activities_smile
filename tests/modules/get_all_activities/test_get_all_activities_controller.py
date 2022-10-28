from src.helpers.http_models import HttpRequest, HttpResponse
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.get_all_activities.get_all_activities_controller import GetAllActivitiesController
from src.modules.get_all_activities.get_all_activities_usecase import GetAllActivitiesUsecase
from src.modules.get_all_activities.get_all_activities_viewmodel import GetAllActivitiesViewmodel


class Test_GetAllActivitiesController:

    def test_get_activity(self):
        repo = ActivityRepositoryMock()
        usecase = GetAllActivitiesUsecase(repo)
        controller = GetAllActivitiesController(usecase)

        httpRequest = HttpRequest()

        httpResponse = controller(httpRequest)
        viewModel = GetAllActivitiesViewmodel(repo.activities)
        assert httpResponse.status_code == 200
        assert httpResponse.body == viewModel.to_dict()

    def test_get_all_activities_no_content(self):
        repo = ActivityRepositoryMock()
        repo.activities = []
        usecase = GetAllActivitiesUsecase(repo)
        controller = GetAllActivitiesController(usecase)

        httpRequest = HttpRequest()

        httpResponse = controller(httpRequest)
        assert httpResponse.status_code == 204

from src.helpers.http_models import OK, HttpRequest, NoContent
from src.modules.get_all_activities.get_all_activities_usecase import GetAllActivitiesUsecase
from src.modules.get_all_activities.get_all_activities_viewmodel import GetAllActivitiesViewmodel


class GetAllActivitiesController:

    def __init__(self, usecase: GetAllActivitiesUsecase):
        self.usecase = usecase

    def __call__(self, request: HttpRequest):
        response = self.usecase()
        if len(response) == 0:
            return NoContent()

        viewModel = GetAllActivitiesViewmodel(response)
        return OK(body=viewModel.to_dict())


from dataclasses import MISSING
from src.domain.entities.activity import Activity
from src.helpers.errors import MISSING_FIELD
from src.helpers.http_models import OK, HttpRequest, HttpResponse, NoContent
from src.helpers.http_status_code import HttpStatusCode
from src.modules.get_all_activities.get_all_activities_usecase import GetAllActivitiesUsecase
from src.modules.get_all_activities.get_all_activity_viewmodel import GetAllActivitiesViewmodel


class GetAllActivitiesController:

    def __init__(self, usecase: GetAllActivitiesUsecase):
        self.usecase = usecase

    def __call__(self, request: HttpRequest):

        try:
            response = self.usecase()
            if len(response) == 0:
                return NoContent()

            viewModel = GetAllActivitiesViewmodel(response)
            return OK(body=viewModel.to_dict())

        except MISSING_FIELD as err:
            return HttpResponse(
                status_code=HttpStatusCode.INTERNAL_SERVER_ERROR.value,
                body=err.message
            )

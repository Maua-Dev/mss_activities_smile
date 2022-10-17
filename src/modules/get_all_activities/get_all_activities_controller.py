from src.helpers.http_models import OK, HttpRequest, HttpResponse, InternalServerError
from src.modules.get_all_activities.get_all_activities_usecase import GetAllActivitiesUsecase


class GetAllActivitiesController:

    def __init__(self, usecase: GetAllActivitiesUsecase):
        self.usecase = usecase

    def __call__(self, request: HttpRequest):
        try:

            response = self.usecase()

            return OK(body=response.__dict__)

        except Exception as e:
            return InternalServerError()



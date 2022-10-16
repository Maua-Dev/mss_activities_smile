from dataclasses import MISSING
from src.domain.entities.activity import Activity
from src.helpers.errors import MISSING_FIELD
from src.helpers.http_models import Created, HttpRequest, HttpResponse
from src.helpers.http_status_code import HttpStatusCode
from src.modules.get_activity.get_activity_usecase import GetActivityUsecase


class GetActivityController:

    def __init__(self, usecase: GetActivityUsecase):
        self.usecase = usecase

    def __call__(self, request: HttpRequest):

        try:

            activity = request.body

            activity_code = activity.get("code")
            if not activity_code or activity_code == '':
                raise MISSING_FIELD("code")

            response = self.usecase(activity_code)

            if not activity.get('initialDate'):
                raise MISSING_FIELD("initialDate")

            self.usecase(activity)

            return Created()

        except MISSING_FIELD as err:
            return HttpResponse(
                status_code=HttpStatusCode.INTERNAL_SERVER_ERROR.value,
                body=err.message
            )
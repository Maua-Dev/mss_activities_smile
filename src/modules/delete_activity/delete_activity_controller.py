from src.helpers.http_models import OK, HttpRequest, HttpResponse
from src.modules.delete_activity.delete_activity_usecase import DeleteActivityUsecase
from src.helpers.errors import MISSING_FIELD
from src.helpers.http_models import HttpRequest, HttpResponse, BadRequest, InternalServerError


class DeleteActivityController:
    def __init__(self, usecase: DeleteActivityUsecase):
        self.usecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            activity = request.body

            activity_code = activity.get('code')
            if not activity_code or activity_code == '':
                raise MISSING_FIELD("code")

            res = self.usecase(code=activity_code)
            if res:
                return OK(body=f'Activity with code {activity_code} deleted')
            else:
                return InternalServerError(body='Internal Server Error')

        except MISSING_FIELD as e:
            return BadRequest(body=e.args[0])

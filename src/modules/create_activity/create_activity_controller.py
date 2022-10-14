from src.helpers.http_models import HttpRequest, HttpResponse, Created, BadRequest, InternalServerError
from src.modules.create_activity.create_activity_usecase import CreateActivityUsecase
from src.helpers.errors import MISSING_FIELD


class CreateActivityController:

    def __init__(self, usecase: CreateActivityUsecase):
        self.usecase = usecase

    def __call__(self, request: HttpRequest):
        try:
            activity = request.body

            activity_code = activity.get('code')
            if not activity_code or activity_code == '':
                raise MISSING_FIELD("code")

            if not activity.get('initialDate'):
                raise MISSING_FIELD("initialDate")

            self.usecase(activity)

            return Created()

        except MISSING_FIELD as e:
            return BadRequest(body=e.args[0])
        except:
            return InternalServerError(body='Internal Server Error')

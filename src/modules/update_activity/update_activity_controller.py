from src.domain.entities.activity import Activity
from src.helpers.http_models import HttpRequest, HttpResponse, Created, BadRequest, InternalServerError
from src.modules.update_activity.update_activity_usecase import UpdateActivityUsecase
from src.helpers.errors import MISSING_FIELD


class UpdateActivityController:

    def __init__(self, usecase: UpdateActivityUsecase):
        self.usecase = usecase

    def __call__(self, request: HttpRequest):
        try:
            # activity_on_body = request.body
            # activity = Activity()
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
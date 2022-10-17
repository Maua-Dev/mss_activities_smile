from src.helpers.http_models import HttpRequest, HttpResponse
from src.modules.get_all_activities.get_activity_by_code_usecase import ACTIVITY_NOT_FOUND, GetActivityByCodeUsecase


class GetActivityByCodeController:

    def __init__(self, usecase: GetActivityByCodeUsecase):
        self.usecase = usecase

    def __call__(self, request: HttpRequest):
        try:
            code = request.query_params.get("code")

            if not code:
                raise Exception("code is required")

            response = self.usecase(code)

            return HttpResponse(body=response.__dict__)

        except ACTIVITY_NOT_FOUND as e:
            return HttpResponse(body={"message": e.message}, status_code=404)

        except Exception as e:
            return HttpResponse(body={"message": e.args[0]}, status_code=500)



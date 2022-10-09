from src.helpers.http_models import HttpRequest, HttpResponse
from src.modules.get_activity_by_code.get_activity_by_code_usecase import ACTIVITY_NOT_FOUND, GetActivityByCodeUsecase


'''
O certo seria eu escrever os HTTPs responses dentro do helpers/http_models? que nem o vilard fez com o 200
que nem aqui https://github.com/Maua-Dev/appmaua_subjects/blob/main/src/modules/get_subject/get_subject_controller.py

Eu deveria, além do 200, incluir outros tipos de erro (aqui no controller e uma classe no USECASE)




principais:
https://www.restapitutorial.com/httpstatuscodes.html

'''


class GetActivityByCodeController:

    def __init__(self, usecase: GetActivityByCodeUsecase):
        self.usecase = usecase

    def __call__(self, request: HttpRequest):
        try:
            code = request.query_params.get("code")

            if not code:
                raise Exception("code is required")

            response = self.usecase(code)
            #caso 200
            return HttpResponse(body=response.__dict__)

        except ACTIVITY_NOT_FOUND as e:
            return HttpResponse(
                body={"message": e.message},
                status_code=404
            )

        except Exception as e:
            return HttpResponse(
                body={"message": e.args[0]},
                status_code=500
            )

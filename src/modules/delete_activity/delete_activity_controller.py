from src.helpers.http_models import HttpRequest, HttpResponse
from src.modules.delete_activity.delete_activity_usecase import DeleteActivityUsecase
from src.helpers.errors import MISSING_FIELD
from src.helpers.http_models import HttpRequest, HttpResponse, Created, BadRequest, InternalServerError
class DeleteActivityController:
    def __init__(self, usecase: DeleteActivityUsecase):
        self.usecase = usecase
        # self.DeleteActivityUsecase = usecase / dá na mesma?

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            activity = request.body

            activity_code = activity.get('code')
            if not activity_code or activity_code == '':
                raise MISSING_FIELD("code")

            if not activity.get('initialDate'):
                raise MISSING_FIELD("initialDate")
            
            activity = self.DeleteActivityUsecase ( 
                code = request.query_params.get('code'),
                initialDate= request.query_params.get('initialDate'),
                )
          
            return Created()

        except MISSING_FIELD as e:
            return BadRequest(body=e.args[0])
        except:
            return InternalServerError(body='Internal Server Error')




        

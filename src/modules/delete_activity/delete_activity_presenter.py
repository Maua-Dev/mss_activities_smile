from src.domain.repositories.activity_repository_interface import ActivityRepository
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.delete_activity.delete_activity_usecase import DeleteActivityUsecase
from src.modules.delete_activity.delete_activity_controller import DeleteActivityController
from src.helpers.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


async def lambda_handler(event, context):
    repo = ActivityRepositoryMock()
    usecase = DeleteActivityUsecase(repo)
    controller = DeleteActivityController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)

    HttpResponse = LambdaHttpResponse(
        status_code=response.status_code,
        body=response.body,
        headers=response.headers
    )

    return HttpResponse.toDict()

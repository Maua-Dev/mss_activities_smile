from src.helpers.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.create_activity.create_activity_controller import CreateActivityController
from src.modules.create_activity.create_activity_usecase import CreateActivityUsecase


async def lambda_handler(event, context):
    repo = ActivityRepositoryMock()
    usecase = CreateActivityUsecase(repo)
    controller = CreateActivityController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = await controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

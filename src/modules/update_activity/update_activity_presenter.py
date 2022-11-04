from src.helpers.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.update_activity.update_activity_controller import UpdateActivityController
from src.modules.update_activity.update_activity_usecase import UpdateActivityUsecase

async def lambda_handler(event, context):
    repo = ActivityRepositoryMock()
    usecase = UpdateActivityUsecase(repo)
    controller = UpdateActivityController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = await controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
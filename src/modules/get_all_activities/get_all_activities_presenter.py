import asyncio

from src.helpers.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.get_all_activities.get_all_activities_controller import GetAllActivitiesController
from src.modules.get_all_activities.get_all_activities_usecase import GetAllActivitiesUsecase

# SubjectRepositoryDynamo() a ser criado 
async def lambda_handler(event, context):
    usecase = GetAllActivitiesUsecase(repo)
    controller = GetAllActivitiesController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = await controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
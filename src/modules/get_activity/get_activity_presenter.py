import asyncio

from src.helpers.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock, Test_ActivityRepositoryMock
from src.modules.get_activity.get_activity_controller import GetActivityController
from src.modules.get_activity.get_activity_usecase import GetActivityUsecase
#envs a ser criada (?)
#from src.envs import Envs

# SubjectRepositoryDynamo() a ser criado 
async def lambda_handler(event, context):
    #repo = SubjectRepositoryMock() if Envs.IsMock() else SubjectRepositoryDynamo()
    repo = ActivityRepositoryMock()
    usecase = GetActivityUsecase(repo)
    controller = GetActivityController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = await controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
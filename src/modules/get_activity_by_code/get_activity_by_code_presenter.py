import asyncio

from src.helpers.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.infra.repositories.activity_repository_mock import SubjectRepositoryMock
from src.modules.get_activity_by_code.get_activity_by_code_controller import GetActivityByCodeController
from src.modules.get_activity_by_code.get_activity_by_code_usecase import GetActivityByCodeUsecase
#envs a ser criada (?)
#from src.envs import Envs

# SubjectRepositoryDynamo() a ser criado 
async def lambda_handler(event, context):
    #repo = SubjectRepositoryMock() if Envs.IsMock() else SubjectRepositoryDynamo()
    usecase = GetActivityByCodeUsecase(repo)
    controller = GetActivityByCodeController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = await controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
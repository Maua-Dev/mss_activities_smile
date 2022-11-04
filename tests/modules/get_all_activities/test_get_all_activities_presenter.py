# import pytest

# class Test_GetAllSubjectsPresenter:

#     def test_get_all_activities(self):

#         event = {
#           "version": "2.0",
#           "routeKey": "$default",
#           "rawPath": "/my/path",
#           "rawQueryString": None,
#           "cookies": [
#             "cookie1",
#             "cookie2"
#           ],
#           "headers": {
#             "header1": "value1",
#             "header2": "value1,value2"
#           },
#           "queryStringParameters": {
#             "parameter2": "value"
#           },
#           "requestContext": {
#             "accountId": "123456789012",
#             "apiId": "<urlid>",
#             "authentication": None,
#             "authorizer": {
#                 "iam": {
#                         "accessKey": "AKIA...",
#                         "accountId": "111122223333",
#                         "callerId": "AIDA...",
#                         "cognitoIdentity": None,
#                         "principalOrgId": None,
#                         "userArn": "arn:aws:iam::111122223333:user/example-user",
#                         "userId": "AIDA..."
#                 }
#             },
#             "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
#             "domainPrefix": "<url-id>",
#             "http": {
#               "method": "GET",
#               "path": "/my/path",
#               "protocol": "HTTP/1.1",
#               "sourceIp": "123.123.123.123",
#               "userAgent": "agent"
#             },
#             "requestId": "id",
#             "routeKey": "$default",
#             "stage": "$default",
#             "time": "12/Mar/2020:19:03:58 +0000",
#             "timeEpoch": 1583348638390
#           },
#           "body": None,
#           "pathParameters": None,
#           "isBase64Encoded": None,
#           "stageVariables": None
#         }

#         from src.modules.get_all_activities.get_all_activities_presenter import lambda_handler

#         response = lambda_handler(event, None)
#         assert response["statusCode"] == 200

        
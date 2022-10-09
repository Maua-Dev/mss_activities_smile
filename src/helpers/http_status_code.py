from enum import Enum


class HttpStatusCode(Enum):
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    #REDIRECT = 303
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    #NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    
    INTERNAL_SERVER_ERROR = 500 #quando não é nenhum dos outros erros
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504
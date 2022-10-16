from src.helpers.http_status_code import HttpStatusCode
from typing import Any

class HttpRequest:
    body: dict
    headers: dict
    query_params: dict
    status_code: int

    def __init__(self,body: dict = None, headers: dict = None, query_params: dict = None):
        
        self.body = body
        self.headers = headers
        self.query_params = query_params


class HttpResponse:
    body: dict
    status_code: int
    headers: dict 

    def __init__(self, status_code: int, body: dict = None, headers: dict = None):
        self.status_code = status_code
        self.body = body
        self.headers = headers




class OK(HttpResponse):
    def __init__(self, body: Any) -> None:
     super().__init__(HttpStatusCode.OK.value, body)


class Created(HttpResponse):
    def __init__(self) -> None:
        super().__init__(HttpStatusCode.CREATED.value, None)


class NoContent(HttpResponse):
    def __init__(self) -> None:
        super().__init__(HttpStatusCode.NO_CONTENT.value, None)


class InternalServerError(HttpResponse):
    def __init__(self, body: Any) -> None:
        super().__init__(HttpStatusCode.INTERNAL_SERVER_ERROR.value, body)


class NotFound(HttpResponse):
    def __init__(self, body: Any) -> None:
        super().__init__(HttpStatusCode.NOT_FOUND.value, body)
        

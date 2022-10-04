

class HttpRequest:
    body: dict
    headers: dict
    query_params: dict

    def __init__(self, body: dict = None, headers: dict = None, query_params: dict = None):
        self.body = body
        self.headers = headers
        self.query_params = query_params


class HttpResponse:
    body: dict
    status_code: int

    def __init__(self, body: dict = None, status_code: int = 200):
        self.body = body
        self.status_code = status_code

    def __call__(self, *args, **kwargs):
        return self.body, self.status_code
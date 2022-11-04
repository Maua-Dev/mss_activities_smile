from src.helpers.errors.base_errors import BaseError

class EntityError(BaseError):
    def __init__(self, message: str):
        super().__init__(f'Field {message} is not valid')
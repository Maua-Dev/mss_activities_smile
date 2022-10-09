from http.client import NOT_FOUND
from src.domain.entities.activity import Activity
from src.domain.repositories.activity_repository_interface import IActivityRepository



class GetActivityByCodeUsecase:

    def __init__(self, activity_repository: IActivityRepository):
        self.activity_repository = activity_repository

    def __call__(self, code) -> Activity:
        if code == "Banana":
            raise Exception("Banana is not a valid code")

        activity = self.activity_repository.get_activity_by_code(code)

        if activity is None:
            raise NOT_FOUND(f"Activity with code {code} was not found")

        return activity


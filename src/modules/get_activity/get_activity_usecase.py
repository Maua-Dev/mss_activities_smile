from http.client import NOT_FOUND
from src.domain.entities.activity import Activity
from src.domain.repositories.activity_repository_interface import IActivityRepository



class GetActivityUsecase:

    def __init__(self, activity_repository:IActivityRepository) -> None:
        self.activity_repository = activity_repository

    def __call__(self, activity) -> bool:
        
        return self.activity_repository.get_activity(activity)

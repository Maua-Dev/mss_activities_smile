from src.domain.entities.activity import Activity
from src.domain.repositories.activity_repository_interface import IActivityRepository

class UpdateActivityUsecase:

    def __init__(self, activity_repository: IActivityRepository) -> None:
        self.activity_repository = activity_repository

    def __call__(self, activity) -> Activity:
        return self.activity_repository.update_activity(activity)
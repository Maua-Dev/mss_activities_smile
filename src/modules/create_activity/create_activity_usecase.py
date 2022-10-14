from src.domain.entities.activity import Activity
from src.domain.repositories.activity_repository_interface import IActivityRepository


class CreateActivityUsecase:

    def __init__(self, activity_repository: IActivityRepository) -> None:
        self.activity_repository = activity_repository

    def __call__(self, activity) -> bool:
        return self.activity_repository.create_activity(activity)

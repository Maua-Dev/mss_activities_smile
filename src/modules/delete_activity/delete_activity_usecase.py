from src.domain.entities.activity import Activity
from src.domain.repositories.activity_repository_interface import IActivityRepository


class DeleteActivityUsecase:

        def __init__(self, activity_repository:IActivityRepository) -> None:
            self.activity_repository = activity_repository
        
        def __call__(self, activity) -> bool:
            activity = self.activity_repository.delete_activity(activity)
            return activity
            
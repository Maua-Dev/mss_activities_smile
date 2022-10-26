from src.domain.repositories.activity_repository_interface import IActivityRepository


class GetAllActivitiesUsecase:

    def __init__(self, activity_repository: IActivityRepository) -> None:
        self.activity_repository = activity_repository

    def __call__(self, activity) -> bool:
        activity = self.activity_repository.get_all_activities()
        return activity

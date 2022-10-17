from typing import List
from src.domain.entities.activity import Activity
from src.domain.repositories.activity_repository_interface import IActivityRepository

class GetAllActivitiesUsecase:

    def __init__(self, activity_repository: IActivityRepository):
        self.activity_repository = activity_repository

    def __call__(self) -> List[Activity]:
        activities = self.activity_repository.get_all_activities()
        return activities


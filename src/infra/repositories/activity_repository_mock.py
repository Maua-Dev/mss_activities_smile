from typing import List

from src.domain.entities.activity import Activity
from src.domain.repositories.activity_repository_interface import IActivityRepository


class ActivityRepositoryMock(IActivityRepository):
    activities: List[Activity]

    def __init__(self):
        self.activities = [
            Activity("Atividade 1", "Tipo 1", "Código 1", "Descrição 1", "2021-01-01", "2021-01-02"),
            Activity("Atividade 2", "Tipo 1", "Código 2", "Descrição 2", "2021-01-01", "2021-01-02"),
            Activity("Atividade 3", "Tipo 3", "Código 3", "Descrição 3", "2021-01-01", "2021-01-02")
        ]

    def get_all_activities(self) -> List[Activity]:
        return self.activities

    def get_activity_by_code(self, activityCode: str) -> Activity:
        for activity in self.activities:
            if activity.code == activityCode:
                return activity

        return None


    def get_activities_by_type(self, type: str) -> List[Activity]:
        activities_aux = []

        for activity in self.activities:
            if activity.type == type:
                activities_aux.append(activity)

        return activities_aux

    def update_activity(self, activityUpdate: Activity) -> Activity: 
        aux = []

        for activity in self.activities:
            if activityUpdate.code == activity.code:
                aux.append(activityUpdate)
            else:
                aux.append(activity)

        self.activities = aux
        return activityUpdate
        
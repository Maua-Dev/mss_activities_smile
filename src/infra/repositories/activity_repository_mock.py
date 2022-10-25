from typing import List

from src.domain.entities.activity import Activity
from src.domain.repositories.activity_repository_interface import IActivityRepository


class ActivityRepositoryMock(IActivityRepository):
    activities: List[Activity]

    def __init__(self):
        self.activities = [
            Activity("Atividade 1", "Tipo 1", "Código 1", "Descrição 1", "2021-01-01", "2021-01-02",
                     "Palestra", "Nome Sobrenome 1", True, "H201", "https://zoom.com/etc/1/", True, '40'),

            Activity("Atividade 2", "Tipo 2", "Código 2", "Descrição 2", "2021-01-01", "2021-01-02",
                     "Palestra", "Nome Sobrenome 2", True, "H202", "https://zoom.com/etc/3/", True, '33'),

            Activity("Atividade 3", "Tipo 3", "Código 3", "Descrição 3", "2021-01-01", "2021-01-03",
                     "Palestra", "Nome Sobrenome 3", True, "H203", "https://zoom.com/etc/3/", False, '100'),

            Activity("Atividade 4", "Tipo 3", "Código 4", "Descrição 3", "2021-01-01", "2021-01-03",
                     "Palestra", "Nome Sobrenome 3", True, "H204", "https://zoom.com/etc/4/", True, '100'),

            Activity("Atividade 5", "Tipo 2", "Código 5", "Descrição 4", "2021-01-01", "2021-01-03",
                     "Workshop", "Nome Sobrenome 3", True, "H205", "https://zoom.com/etc/5/", False, '100'),

            Activity("Atividade 6", "Tipo 1", "Código 6", "Descrição 5", "2021-01-01", "2021-01-03",
                     "Palestra", "Nome Sobrenome 3", True, "H206", "https://zoom.com/etc/6/", True, '12'),

            Activity("Atividade 7", "Tipo 3", "Código 7", "Descrição 6", "2021-01-01", "2021-01-03",
                     "Workshop", "Nome Sobrenome 3", True, "H207", "https://zoom.com/etc/7/", True, '45'),

            Activity("Atividade 8", "Tipo 1", "Código 8", "Descrição 7", "2021-01-01", "2021-01-03",
                     "Palestra", "Nome Sobrenome 3", True, "H208", "https://zoom.com/etc/8/", False, '100'),

            Activity("Atividade 9", "Tipo 2", "Código 9", "Descrição 8", "2021-01-01", "2021-01-03",
                     "Palestra", "Nome Sobrenome 3", True, "H209", "https://zoom.com/etc/9/", True, '50')

        ]

    def get_all_activities(self) -> List[Activity]:
        return self.activities

    def get_activity_by_code(self, activityCode: str) -> Activity:
        for activity in self.activities:
            if activity.code == activityCode:
                return activity

        return None

    def delete_activity(self, code: str) -> bool:
        activities_aux = []

        for activity in self.activities:
            if activity.code != code:
                activities_aux.append(activity)
        self.activities = activities_aux
        return True


from abc import ABC, abstractmethod
from typing import List, Tuple
from src.domain.entities.activity import Activity


class IActivityRepository(ABC):  # todo implementar os metodos

    @abstractmethod
    def get_all_activities(self) -> List[Activity]:
        pass

    @abstractmethod
    def get_activity_by_code(self, activity_code: str) -> Activity:
        pass

    @abstractmethod
    def delete_activity(self, code: str) -> bool:
        pass

    @abstractmethod
    def create_activity(self, activity: Activity) -> bool:
        pass

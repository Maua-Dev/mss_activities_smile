
from abc import ABC, abstractmethod
from typing import List, Tuple
from src.domain.entities.activity import Activity


class v(ABC):  # todo implementar os metodos

    @abstractmethod
    def get_all_activities(self) -> List[Activity]:
        pass

    @abstractmethod
    def get_activity_by_code(self, activityCode: str) -> Activity:
        pass

    @abstractmethod
    def delete_activity(self, code: str) -> bool:
        pass

    def get_activities_by_type(self, type: str) -> List[Activity]:
        pass

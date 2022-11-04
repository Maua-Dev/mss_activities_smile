
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
<<<<<<< HEAD
    def get_activities_by_type(self, type: str) -> List[Activity]:
        pass

    @abstractmethod
    def update_activity(self, type: str) -> bool:
        pass
=======
    def delete_activity(self, code: str) -> bool:
        pass

    @abstractmethod
    def create_activity(self, activity: Activity) -> bool:
        pass
>>>>>>> d3464796e57b55bc7ae5cb668b78098a4fc2f4ec

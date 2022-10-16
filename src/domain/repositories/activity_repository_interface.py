
from abc import ABC, abstractmethod
from typing import List, Tuple
from src.domain.entities.activity import Activity


class IActivityRepository(ABC): #todo implementar os metodos

    @abstractmethod
    def get_all_activities(self) -> List[Activity]:
        pass

    @abstractmethod
    def get_activity_by_code(self, activityCode:str) -> Activity:
        pass
    
    #Aqui não seria get_activities_by_initialDate? Pq aqui e no mock foi usado o by_type??
    @abstractmethod
    def get_activities_by_type(self, type: str) -> List[Activity]:
        pass
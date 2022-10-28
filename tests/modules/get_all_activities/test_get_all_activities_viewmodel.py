import pytest
from src.modules.get_all_activities.get_all_activities_viewmodel import GetAllActivitiesViewmodel
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
class Test_GetAllSubjectsViewModel:
    def test_get_all_activities_view_model(self): 
        repo = ActivityRepositoryMock()
        activitiesViewModel = GetAllActivitiesViewmodel(repo.activities).to_dict()
        activityViewModel = activitiesViewModel[0]
        result = {
            'activityCode': "Código 1",
            'type': "Tipo 1",
            'title': "Atividade 1",
            'description': "Descrição 1",
            'schedule': {
                'date': "2021-01-01",
                'totalParticipants': "40",
                'duration': "2021-01-02", #checar 
                'location': "H201",
                'link': "https://www.zoom.com/etc/1/",
                'acceptSubscription': True
                # 'enrolledUsers': self.enrolledUsers
                },
            'speakers': "Nome Sobrenome 1"
        }


        assert activityViewModel == result

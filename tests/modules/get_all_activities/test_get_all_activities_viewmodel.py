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
            'schedule': [{
                'date': 1663668000.0,
                'totalParticipants': 100,
                'duration': 3600000.0,
                'location': "H201",
                'link': "https://zoom.com/etc/1/",
                'acceptSubscription': True
                }],
            'speakers': [{
                'name': 'Nome Sobrenome 1',
                'bio': 'bla bla bla',
                'company': 'Dev Community Mauá'
            }]
        }

        assert activityViewModel == result

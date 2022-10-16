import pytest
from src.domain.entities.activity import Activity
from src.helpers.errors import MISSING_FIELD
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.get_activity.get_activity_usecase import GetActivityUsecase, ACTIVITY_NOT_FOUND
from  src.helpers.errors import MISSING_FIELD

class Test_GetActivityUsecase:

    def test_get_activity_usecase(self):
        repo = ActivityRepositoryMock()
        usecase = GetActivityUsecase(repo=repo)

        
        activity = usecase(code = "Código 1", initialDate = "2021-01-01")
       
        assert activity == repo.activities[0]

    def test_get_activity_not_found(self):
        repo = ActivityRepositoryMock()
        usecase = GetActivityUsecase(repo)

        with pytest.raises(MISSING_FIELD) as e:
            activity = usecase(code='Código 999', initialDate='2029-01-01')

    '''
    to do:

    definir diferentes erros em src/helpers/errors.py 
    testar aqui

    '''
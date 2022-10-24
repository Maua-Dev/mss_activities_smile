import pytest
from src.domain.entities.activity import Activity
from src.helpers.errors import MISSING_FIELD
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.delete_activity.delete_activity_usecase import DeleteActivityUsecase
from  src.helpers.errors import MISSING_FIELD

class Test_DeleteActivityUsecase:

    def test_delete_activity_usecase(self):
        repo = ActivityRepositoryMock()
        usecase = DeleteActivityUsecase(repo=repo)
        res = usecase(code = "Código 1")
       
        assert repo.activities[0] != "Código 1"
        assert res
        










    '''
    to do:

    definir diferentes erros em src/helpers/errors.py 
    testar aqui
    
    '''
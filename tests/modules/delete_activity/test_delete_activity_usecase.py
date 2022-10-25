from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.delete_activity.delete_activity_usecase import DeleteActivityUsecase



class Test_DeleteActivityUsecase:

    def test_delete_activity_usecase(self):
        repo = ActivityRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        res = usecase(code="Código 1")

        assert repo.activities[0] != "Código 1"
        assert res

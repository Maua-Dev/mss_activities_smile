import pytest

from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.get_activity_by_code.get_activity_by_code_usecase import GetActivityByCodeUsecase, ACTIVITY_NOT_FOUND


class Test_GetActivityByCodeUsecase:

    def test_get_activity(self):
        repo = ActivityRepositoryMock()
        usecase = GetActivityByCodeUsecase(repo)

        activity = usecase("Código 1")


        assert activity == repo.activities[0]

    def test_get_activity_not_found(self):
        repo = ActivityRepositoryMock()
        usecase = GetActivityByCodeUsecase(repo)

        with pytest.raises(ACTIVITY_NOT_FOUND) as e:
            usecase("Código 4")
import datetime

from src.domain.entities.activity import Activity
from src.domain.entities.schedule import Schedule
from src.domain.entities.speaker import Speaker
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.update_activity.update_activity_usecase import UpdateActivityUsecase
import pytest

class Test_UpdateActivityUsecase:

    def test_update_activity_usecase_description(self):
        repo  = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo=repo)

        usecase(code="Código 1", new_description="Descrição Nova")

        assert repo.activities[0].description == "Descrição Nova"

    def test_update_activity_usecase_not_found_code(self):
        repo  = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo=repo)

        with pytest.raises(NoItemFound):
            usecase(code="Código 1")

    def test_update_activity_usecase_invalid_code(self):
        repo  = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(
                code="Código 1",
                new_description="Descrição Nova"
            )

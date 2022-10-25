import pytest

from src.domain.entities.activity import Activity
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.create_activity.create_activity_usecase import CreateActivityUsecase


class Test_CreateActivityUsecase:

    def test_create_activity(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo)

        new_activity = Activity("Atividade 4", "Tipo 4", "Código 4", "Descrição 4", "2021-01-01", "2021-01-02"),
        usecase(new_activity)

        assert repo.activities[-1] == new_activity

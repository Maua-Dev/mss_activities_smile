import pytest
from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_ActivityRepositoryMock:

    def test_get_all_activities(self):
        repo = ActivityRepositoryMock()

        activities = repo.get_all_activities()

        assert activities == repo.activities

    def test_get_activity_by_code(self):
        repo = ActivityRepositoryMock()

        activity = repo.get_activity_by_code("Código 1")
        assert activity == repo.activities[0]

        activity = repo.get_activity_by_code("Código 2")
        assert activity == repo.activities[1]

        activity = repo.get_activity_by_code("Código 3")
        assert activity == repo.activities[2]

        activity = repo.get_activity_by_code("Código 4")
        assert activity == repo.activities[3]


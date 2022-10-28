from src.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.modules.get_all_activities.get_all_activities_usecase import GetAllActivitiesUsecase


class Test_GetAllActivities:

    def test_get_all_activities(self):
        repo = ActivityRepositoryMock()
        usecase = GetAllActivitiesUsecase(repo)

        activities = usecase()

        assert activities == repo.activities

from src.domain.entities.activity import Activity
from src.domain.entities.schedule import Schedule
from src.domain.entities.speaker import Speaker
from src.helpers.http_models import OK, HttpRequest, HttpResponse, Created, BadRequest, InternalServerError
from src.modules.get_all_activities.get_all_activities_viewmodel import ActivityViewModel
from src.modules.update_activity.update_activity_usecase import UpdateActivityUsecase
from src.helpers.errors import MISSING_FIELD


class UpdateActivityController:

    def __init__(self, usecase: UpdateActivityUsecase):
        self.usecase = usecase

    def __call__(self, request: HttpRequest):
        try:
            activity_on_body = request.body

            activity = Activity(
                title=activity_on_body['title'],
                code=activity_on_body['activityCode'],
                description=activity_on_body['description'],
                activityType=activity_on_body['type'],
                speakers=[
                    Speaker(
                        name=speaker['name'],
                        bio=speaker['bio'],
                        company=speaker['company']
                    ) for speaker in activity_on_body['speakers']],
                schedule=[
                    Schedule(
                        initialDate=schedule['initialDate'],
                        duration=schedule['duration'],
                        maxParticipants=schedule['totalParticipants'],
                        location=schedule['duration'],
                        remoteRoomUrl=schedule['link'],
                        acceptSubscription=schedule['acceptSubscription'],
                        acceptSubscriptionUntilDate=None,
                        finalDate=None
                    ) for schedule in activity_on_body['schedule']
                ]
            )

            activity_updated = self.usecase(activity)
            viewModel = ActivityViewModel(activity_updated)
            return OK(body =viewModel.to_dict())

        except MISSING_FIELD as e:
            return BadRequest(body=e.args[0])
        except:
            return InternalServerError(body='Internal Server Error')
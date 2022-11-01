from src.domain.entities.activity import Activity
from src.domain.entities.schedule import Schedule
from src.domain.entities.speaker import Speaker
from src.helpers.http_models import HttpRequest, HttpResponse, Created, BadRequest, InternalServerError
from src.modules.create_activity.create_activity_usecase import CreateActivityUsecase
from src.helpers.errors import MISSING_FIELD


class CreateActivityController:

    def __init__(self, usecase: CreateActivityUsecase):
        self.usecase = usecase

    def __call__(self, request: HttpRequest):
        try:
            activity_on_body = request.body

            activity_code = activity_on_body.get('activityCode')
            if not activity_code or activity_code == '':
                raise MISSING_FIELD("activityCode")

            schedules = activity_on_body.get('schedule')
            if not schedules or schedules == {}:
                raise MISSING_FIELD("schedule")

            if False in [
                    True if schedule.get('initialDate')
                    else False for schedule in schedules
            ]:
                raise MISSING_FIELD("initialDate")

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

            self.usecase(activity)

            return Created()

        except MISSING_FIELD as e:
            return BadRequest(body=e.args[0])
        except:
            return InternalServerError(body='Internal Server Error')

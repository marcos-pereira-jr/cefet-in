from flask_restful import Resource, reqparse
from app.infrastructure.util.logz import create_logger
from app.domain.study.study import Study
from app.domain.class_schedule.class_scherdule_service import ClassService
from app.domain.class_schedule.class_schedule import ClassSchedule

from datetime import datetime
from flask import request


class ClassResource(Resource):
    parse = reqparse.RequestParser()

    def __init__(self, service: ClassService):
        self.logger = create_logger()
        self.service = service

    def post(self):
        data = request.json
        classSchedule = ClassSchedule(name=data['name'], start=datetime.fromisoformat(data['start']),
                                      end=datetime.fromisoformat(data['end']))
        self.service.save(classSchedule)
        return {'message': 'class has  been created successfully.'}, 201
    
    def get(self):
        def mapper(entity):
            def mapperCheckin(checkin):
                return {
                    "id": str(checkin['_id']),
                    "name": checkin['name'],
                    "time": checkin['time'].isoformat(),
                    "code": checkin['code']
                }
            return {
                    "id": str(entity['_id']),
                    "name": entity['name'],
                    "start": entity['start'].isoformat(),
                    "end": entity['end'].isoformat(),
                    "checkins": [mapperCheckin(checkin) for checkin in entity['checkins']]
                    }
        return [mapper(entity) for entity in self.service.find_all()]

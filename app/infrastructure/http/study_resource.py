from flask_restful import Resource, reqparse
from app.infrastructure.util.logz import create_logger
from app.domain.study.study import Study
from app.domain.study.study_service import StudyService

from flask import request

class StudyResource(Resource):
    parse = reqparse.RequestParser()

    def __init__(self, service : StudyService):
        self.logger = create_logger()
        self.service = service
    
    def post(self):
        data = request.json 
        study = Study(data['uncheck-user-id'] ,data['name'], data['code'])
        self.service.save(study)
        return {'message': 'message has been created successfully.'}, 201

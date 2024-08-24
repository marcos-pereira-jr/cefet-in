from flask_restful import Resource, reqparse
from app.infrastructure.util.logz import create_logger
from app.infrastructure.database.uncheck_repository import UncheckRepository
from app.domain.uncheck_user.uncheck_user_service import UncheckUserService

from flask import request

class UncheckUserResource(Resource):
    parse = reqparse.RequestParser()

    def __init__(self, service : UncheckUserService):
        self.logger = create_logger()
        self.service = service
    
    def get(self):
        def mapper(uncheck):
            return {
                "id":  str(uncheck['_id']),
                "deviceId": uncheck['deviceId']
            }
            
        self.logger.info(" request receive for list uncheck users")
        return [mapper(uncheck) for uncheck in self.service.find_all()]

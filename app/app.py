from flask import Flask
from flask_restful import Api
from app.infrastructure.http.uncheck_user_resource import UncheckUserResource
from app.infrastructure.http.study_resource import StudyResource
from app.infrastructure.broker.uncheck_user_broker import Checkin
from dynaconf import FlaskDynaconf
from app.config.container_config import container

app = Flask(__name__)
FlaskDynaconf(app)
api = Api(app)

api.add_resource(UncheckUserResource, '/uncheck-user',  resource_class_kwargs={'service': container['uncheckUserService']})
api.add_resource(StudyResource, '/user', resource_class_kwargs={'service': container['studyService']})
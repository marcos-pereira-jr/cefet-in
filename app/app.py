from flask import Flask
from flask_restful import Api
from app.infrastructure.http.uncheck_user_resource import UncheckUserResource
from app.infrastructure.http.study_resource import StudyResource
from dynaconf import FlaskDynaconf
from app.config.container_config import container
from app.infrastructure.http.class_uncherdule_resource import ClassResource

app = Flask(__name__)
FlaskDynaconf(app)
api = Api(app)

api.add_resource(UncheckUserResource, '/uncheck-user',  resource_class_kwargs={'service': container['uncheckUserService']})
api.add_resource(StudyResource, '/user', resource_class_kwargs={'service': container['studyService']})
api.add_resource(ClassResource,'/class',resource_class_kwargs={'service':container['classService']})

if __name__ == '__main__':
    app.run(debug=True)

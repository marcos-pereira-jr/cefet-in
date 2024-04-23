from app.infrastructure.database.mongo import mongo
from app.infrastructure.database.uncheck_repository import UncheckRepository
from app.infrastructure.database.study_repository import StudyRepository
from app.domain.uncheck_user.uncheck_user_service import UncheckUserService
from app.infrastructure.http.uncheck_user_resource import UncheckUserResource
from app.infrastructure.http.study_resource import StudyResource
from app.domain.study.study_service import StudyService
from app.infrastructure.broker.uncheck_user_broker import Checkin

container = {}
container['mongo'] = mongo
container['uncheckRepository'] = UncheckRepository(container['mongo'])
container['uncheckUserService'] = UncheckUserService(container['uncheckRepository'])
container['studyRepository'] = StudyRepository(container['mongo'])
container['studyService'] = StudyService(repository=container['studyRepository'],
                                         uncheckUserService=container['uncheckUserService'])
container['broker'] = Checkin(container['uncheckUserService'])
container['broker'].run()
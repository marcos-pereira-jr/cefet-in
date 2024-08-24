from app.infrastructure.database.mongo import mongo
from app.infrastructure.database.uncheck_repository import UncheckRepository
from app.infrastructure.database.class_repository import ClassRepository
from app.domain.class_schedule.class_scherdule_service import ClassService
from app.infrastructure.database.study_repository import StudyRepository
from app.domain.uncheck_user.uncheck_user_service import UncheckUserService
from app.domain.study.study_service import StudyService
from app.infrastructure.broker.uncheck_user_broker import Checkin

container = {}
container['mongo'] = mongo
container['uncheckRepository'] = UncheckRepository(container['mongo'])
container['uncheckUserService'] = UncheckUserService(container['uncheckRepository'])

container['studyRepository'] = StudyRepository(container['mongo'])
container['studyService'] = StudyService(repository=container['studyRepository'],uncheckUserService =container['uncheckUserService'])

container['classRepository'] = ClassRepository(container['mongo'])
container['classService'] = ClassService(container['studyService'],container['classRepository'])

container['broker'] = Checkin(container['uncheckUserService'])
container['broker'].run()

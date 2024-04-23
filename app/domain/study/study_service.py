from app.infrastructure.database.study_repository import StudyRepository
from app.domain.uncheck_user.uncheck_user_service import UncheckUserService
from app.domain.study.study import Study
from app.infrastructure.util.logz import create_logger

class StudyService():
    
    def __init__(self, repository : StudyRepository, uncheckUserService : UncheckUserService ):
        self.repository = repository
        self.uncheckUserService = uncheckUserService
        self.logger = create_logger(f'[bold purple]Service:[bold yellow]StudyService[/bold yellow][/bold purple]')
        
    def save(self, study : Study):
        uncheck = self.uncheckUserService.find_one(study.uncheckUserId)
        if uncheck is None:
            raise ValueError("Uncheck User not Found")
        self.logger.info(f"Linked study: {study.name} with deviceId: {uncheck.deviceId} 🎓")
        self.repository.save(study)
    
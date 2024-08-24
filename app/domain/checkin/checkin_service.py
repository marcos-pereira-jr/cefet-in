from app.domain.uncheck_user.uncheck_user_service import UncheckUserService
from app.domain.study.study_service import StudyService
from app.domain.class_schedule.class_scherdule_service import ClassService
from app.infrastructure.util.logz import create_logger

class CheckinService:
    def __init__(self, uncheckUserService : UncheckUserService, studyService : StudyService,
                 classService : ClassService ) -> None:
        self.classService = classService
        self.uncheckUserService = uncheckUserService
        self.studyService = studyService
        self.logger = create_logger(f'[bold purple]Service:[bold yellow]CheckinService[/bold yellow][/bold purple]')
 

    def checkin(self, deviceId):
        uncheck_user  = self.uncheckUserService.find_one_by_deviceId(deviceId)
        if uncheck_user == None :
            self.logger.info(f"Device Id not found : {deviceId} 📲")
            self.uncheckUserService.save(deviceId)
        else:
            if(uncheck_user.linked == True):
               study = self.studyService.find_user_by_uncheck_id(uncheck_user._id);
               if study is not None:
                   self.logger.info(f"User found : {study.name} with code {study.code} 👨‍🎓")
                   self.classService.checkin(study)   
               else:
                   self.logger.info(f"User not found with uncheck_user_id {uncheck_user._id} 👨‍🎓")
            else:
                self.logger.info(f"User not checked: {uncheck_user._id} 👨‍🎓")





from app.domain.study.study import Study
from app.domain.study.study_service import StudyService
from app.infrastructure.database.class_repository import ClassRepository;
from app.infrastructure.util.logz import create_logger

class ClassService():
    def __init__(self, studyService : StudyService, classRepository : ClassRepository ):
        self.study_service = studyService
        self.classRepository = classRepository
        self.logger = create_logger(f'[bold purple]Service:[bold yellow]ClassService[/bold yellow][/bold purple]')

        
    def checkin(self, study : Study):
        classSchedule = self.findCurrentClass()
        if (classSchedule is not None):
           self.logger.info(f"Classes registered at the moment {classSchedule.name} 🏫")
           classSchedule.checkin(study)
           self.classRepository.update(classSchedule)
        else:
            self.logger.info(f"No classes registered at the moment 🏫")

    def findCurrentClass(self):
        return self.classRepository.findCurrentClass();

    def save(self, classScherdule):
        return self.classRepository.save(classScherdule)

    def find_all(self):
        return self.classRepository.find_all()

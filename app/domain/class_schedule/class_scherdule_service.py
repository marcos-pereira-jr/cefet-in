

from app.domain.study.study import Study
from app.domain.study.study_service import StudyService
from app.infrastructure.database.class_repository import ClassRepository;

class ClassService():
    def __init__(self, studyService : StudyService, classRepository : ClassRepository ):
        self.study_service = studyService
        self.classRepository = classRepository
        
    def checkin(self, study : Study):
       classSchedule = self.findCurrentClass()
       classSchedule.checkin(study)
    
    def findCurrentClass(self):
        return self.classRepository.findCurrentClass();

    def save(self, classScherdule):
        return self.classRepository.save(classScherdule)

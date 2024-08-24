from dynaconf import settings
from app.domain.study.study import Study

class StudyRepository():
    def __init__(self, mongo):
        self.collection = "study"
        self.mongo = mongo
        
    def find_all(self):
        return self.mongo[settings.get("MONGO_DATABASE")][self.collection].find({})

    def save(self, study : Study):
        return self.mongo[settings.get("MONGO_DATABASE")][self.collection].insert_one(
                {
                    "uncheckUserId": study.uncheckUserId,
                    "name": study.name,
                    "code": study.code
                 })

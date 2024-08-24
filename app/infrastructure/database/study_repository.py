from dynaconf import settings
from app.domain.study.study import Study
from app.infrastructure.util.logz import create_logger

class StudyRepository():
    def __init__(self, mongo):
        self.collection = "study"
        self.mongo = mongo
        self.logger = create_logger(f'[bold green]UserRepository:[bold yellow]{self.collection}[/bold yellow][/bold green]')
    
    def find_all(self):
        return self.mongo[settings.get("MONGO_DATABASE")][self.collection].find({})

    def save(self, study : Study):
        return self.mongo[settings.get("MONGO_DATABASE")][self.collection].insert_one(
                {
                    "uncheckUserId": study.uncheckUserId,
                    "name": study.name,
                    "code": study.code
                 })
    
    def find_user_by_uncheck_id(self, unId):
        self.logger.info(f"Try find a User with uncheck id : { unId } 📲")
        data = self.mongo[settings.get("MONGO_DATABASE")][self.collection].find_one({'uncheckUserId' : str(unId)})
        if data is None: 
            self.logger.info(f"Not Found a User with uncheck id : { unId } 📲")
            return None
        return Study(**data)
 

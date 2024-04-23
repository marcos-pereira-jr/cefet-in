from app.infrastructure.util.logz import create_logger
from dynaconf import settings
from app.domain.uncheck_user.uncheck_user import UncheckUser
from bson.objectid import ObjectId
from typing import Optional


class UncheckRepository():
    def __init__(self, mongo):
        self.collection = "uncheck"
        self.mongo = mongo
        self.logger = create_logger(f'[bold green]Repository:[bold yellow]{self.collection}[/bold yellow][/bold green]')

    def find_all(self):
        return self.mongo[settings.get("MONGO_DATABASE")][self.collection].find({})
    
    def find_one(self, id) -> Optional[UncheckUser]:
        data = self.mongo[settings.get("MONGO_DATABASE")][self.collection].find_one({"_id": ObjectId(id)})
        if data is None: return None
        return UncheckUser(**data)
    
    def find_one_by_deviceId(self, deviceId) -> Optional[UncheckUser]:
        data = self.mongo[settings.get("MONGO_DATABASE")][self.collection].find_one({"deviceId": deviceId})
        if data is None: return None
        return UncheckUser(**data)
        
    def save(self, uncheck : UncheckUser):
        self.logger.info(f"save new uncheck user with deviceId: {uncheck.deviceId} 📲")
        return self.mongo[settings.get("MONGO_DATABASE")][self.collection].insert_one({"deviceId":uncheck.deviceId})


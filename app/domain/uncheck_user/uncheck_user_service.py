from app.infrastructure.database.uncheck_repository import UncheckRepository;
from app.domain.uncheck_user.uncheck_user import UncheckUser
from app.domain.uncheck_user.uncheck_user_service import UncheckRepository
from typing import Optional

class UncheckUserService():
    def __init__(self, repository : UncheckRepository):
        self.repository = repository
    
    def save(self, deviceId):
        self.repository.save(UncheckUser(deviceId))
    
    def find_one(self, id) -> Optional[UncheckUser]:    
        return self.repository.find_one(id)
        
    def find_one_by_deviceId(self, deviceId):
        return self.repository.find_one_by_deviceId(deviceId)
    
    def find_all(self):
        return self.repository.find_all()
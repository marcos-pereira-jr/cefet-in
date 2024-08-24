from datetime import datetime

from bson.objectid import ObjectId
from app.domain import checkin
from app.domain.study.study import Study

class ClassSchedule():
    def __init__(self,name , start: datetime, end: datetime, checkins : list = [], _id: ObjectId = None):
        self._id = _id
        self.name = name
        self.start = start
        self.end = end
        self.checkins = checkins

    def checkin(self, new: Study):
        if not any(study['_id'] == new._id for study in self.checkins):
            self.checkins.append({"_id": new._id,"name":new.name, "code": new.code,"time": datetime.now()})

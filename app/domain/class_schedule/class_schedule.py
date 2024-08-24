from datetime import datetime
from app.domain.study.study import Study


class ClassSchedule():
    def __init__(self, name , start: datetime, end: datetime, checkins : list[Study] = []):
        self.id = id
        self.name = name
        self.start = start
        self.end = end
        self.checkins = checkins

    def checkin(self, study: Study):
        self.checkins.append(study)
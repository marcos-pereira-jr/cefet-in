from pprint import pprint
from datetime import datetime
from dynaconf import settings

from app.infrastructure.util.logz import create_logger
from app.domain.class_schedule.class_schedule import ClassSchedule

class ClassRepository:
    def __init__(self, mongo) -> None:
        self.collection = "class"
        self.mongo = mongo
        self.logger = create_logger(f'[bold green]Repository:[bold yellow]{self.collection}[/bold yellow][/bold green]')

    def findCurrentClass(self):
        current = datetime.now()
        data = self.mongo[settings.get("MONGO_DATABASE")][self.collection].find_one({
            'start': {"$lte": current},
            'end': {'$gte': current}
            })
        if data is None: return None
        return ClassSchedule(**data)
    
    def save(self, classSchedule : ClassSchedule):
        self.logger.info(f"save new class with begin: {classSchedule.start} and end: {classSchedule.end} 🧾")
        pprint(classSchedule)
        
        self.mongo[settings.get("MONGO_DATABASE")][self.collection].insert_one({
            'name': classSchedule.name,
            'start': classSchedule.start,
            'end': classSchedule.end,
            'checkins': classSchedule.checkins
        })
     
    def update(self, classSchedule : ClassSchedule):
        self.logger.info(f"update class with id: {classSchedule._id} 🧾")
        self.mongo[settings.get("MONGO_DATABASE")][self.collection].update_one({"_id": classSchedule._id},
                                                                               { "$set": {"checkins" : classSchedule.checkins}})

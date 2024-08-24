
from bson.objectid import ObjectId


class Study():
    def __init__(self,_id : ObjectId, uncheckUserId, name, code):
        self._id = _id
        self.uncheckUserId = uncheckUserId
        self.name = name
        self.code = code

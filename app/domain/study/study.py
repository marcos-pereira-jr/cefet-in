
from bson.objectid import ObjectId


class Study():
    def __init__(self, uncheckUserId, name, code, _id:ObjectId = None):
        self._id = _id
        self.uncheckUserId = uncheckUserId
        self.name = name
        self.code = code

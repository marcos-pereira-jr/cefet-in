from bson.objectid import ObjectId

class UncheckUser():
    def __init__(self, _id : ObjectId = None, deviceId="" , linked=False):
        self._id = _id
        self.linked = linked
        self.deviceId = deviceId

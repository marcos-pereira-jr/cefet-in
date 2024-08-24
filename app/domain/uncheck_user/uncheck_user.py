from bson.objectid import ObjectId

class UncheckUser():
    def __init__(self, deviceId , _id : ObjectId = None , linked=False):
        self._id = _id
        self.linked = linked
        self.deviceId = deviceId

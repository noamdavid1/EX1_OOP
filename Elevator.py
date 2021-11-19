class Elevator:
    up = 1
    LEVEL = 0
    DOWN = -1
    ERROR = -2

    def __init__(self, _id, _speed, _minFloor, _maxFloor, _closeTime, _openTime, _startTime, _stopTime):
        self._id = _id
        self._speed = _speed
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._closeTime = _closeTime
        self._openTime = _openTime
        self._startTime = _startTime
        self._stopTime = _stopTime

    def MinFloor(self):
        return self._minFloor

    def MaxFloor(self):
        return self._maxFloor

    def TimeForOpen(self):
        return self._openTime

    def TimeForClose(self):
        return self._closeTime

    def getState(self):
        return self.getState()

    def getPos(self):
        pass

    def goTo(self):
        pass

    def getSpeed(self):
        return self._speed

    def getStartTime(self):
        return self._startTime

    def getStopTime(self):
        return self._stopTime

    def getID(self):
        return self._id

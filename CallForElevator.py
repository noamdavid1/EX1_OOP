from Ex1 import elevators, file, building


class CallForElevator:
    UP = 1
    DOWN = 0

    def __init__(self, _time, _getSrc, _getDest, _getState, _getType):
        self._time = _time
        self._getSrc = _getSrc
        self._getDest = _getDest
        self._getState = _getState
        self._getType = _getType

    def getTime(self):
        return self._time

    # Return all values as the formatted list
    def getValuesAsList(self):
        pass

    def getSrc(self):
        return self._getSrc

    def getDest(self):
        return self._getDest

    def getstate(self):
        return self._getState

    def getType(self, DOWN, UP):
        pass

    # Assign the best elevator index
    def allocateAnElevator(self):
        self.call = file
        elevators.sort(key=lambda e: e.getSpeed)
        div_val = (int)(abs(file.Src - file.Dest)) / building.numberOfElevators()
        return elevators[div_val].id

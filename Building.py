class Building:

    def __init__(self, _minFloor, _maxFloor, _elevators=[]):
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._elevators = _elevators.copy()

    def minFloor(self):
        return self._minFloor

    def maxFloor(self):
        return self._maxFloor

    def getElevator(self, index):
        return self._elevators[index]

    def numberOfElevators(self):
        return len(self._elevators)

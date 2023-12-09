from abc import abstractmethod


class DataInterface():

    @abstractmethod
    def setCodeLength(self):
        pass

    @abstractmethod
    def setColorAvailabilities(self):
        pass

    @abstractmethod
    def setCode(self):
        pass

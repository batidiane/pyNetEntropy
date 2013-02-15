

class AbstractAlgorithm:

    def __init__(self, algoname, algotype):
        self.name = algoname
        self.type = algotype
    
    def calculate(self, data):
        raise NotImplementedError
    
    def getName(self):
        return self.name
    
    def getType(self):
        return self.type

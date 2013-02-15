from Algorithm.AbstractAlgorithm import *

class AbstractEntropyAlgorithm(AbstractAlgorithm):
    
    def __init__(self, name):
        AbstractAlgorithm.__init__(self, name, "entropy")
        
    def countCharacters(self, data):
        self.characters = {}
        self.totalCharacters = 0

        for i in data:
            self.totalCharacters += 1
            if i in self.characters:
                self.characters[i] = self.characters[i] + 1
            else:
                self.characters[i] = 1


        
    def getCharacters(self):
        return self.characters
    

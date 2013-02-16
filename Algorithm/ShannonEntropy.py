from Algorithm.AbstractEntropyAlgorithm import *
import math


class ShannonEntropy(AbstractEntropyAlgorithm):
    
    def __init__(self):
        AbstractEntropyAlgorithm.__init__(self, "shannon")
        
    def calculate(self, data):
        self.countCharacters(data)
        entropy = 0
        for occurence in self.characters.values():
            frequency = float(occurence) / self.totalCharacters
            if frequency > 0:
                entropy += frequency * math.log(frequency,2)
        return -entropy
    

from Algorithm.AbstractEntropyAlgorithm import *
import math
import zlib

class KolmogorovEntropy(AbstractEntropyAlgorithm):
    
    def __init__(self):
        AbstractEntropyAlgorithm.__init__(self, "kolmogorov")
        self.type = "complexity"
    
    # Reasonable approximation to the Kolmogorov Complexity
        # using the compression rate
        # ref.: http://lorenzoriano.wordpress.com/tag/python/
    def calculate(self, data):
        l = float(len(data))
        compr = zlib.compress(data)
        c = float(len(compr))
        return c/l
    


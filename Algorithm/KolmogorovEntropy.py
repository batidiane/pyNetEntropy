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
 	# avoiding division by 0
	if l != 0:
            compr = zlib.compress(data)
            c = float(len(compr))
            return c/l
	else:
            return 0

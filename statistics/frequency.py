#!/usr/bin/env python


class Frequency:
    
    def __init__(self):
        self.l_state = 'increase'
        self.pic = 0
        self.t_pic = 0
        self.l_value = 0
        
    def calculate(self, timestamp, value):
    #try to calculate period between two peaks
    #    if value < self.l_value:
    #        decrease = True
    #    else:
    #        decrease = False
    #        res = None
    #    if self.l_state == 'increase':
    #        if decrease:
    #            res = 1/(timestamp - self.t_pic)
    #            self.pic = value
    #            self.t_pic = timestamp
    #    self.l_value = value
    #    if decrease:
    #        self.l_state = 'decrease'
    #    else:
    #        self.l_state = 'increase'
    #    return res
        res= 1/(timestamp - self.t_pic)
        self.t_pic = timestamp
        return res
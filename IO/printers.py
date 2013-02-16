#!/usr/bin/env python
import sys

default_printer_class = 'IO.rfile.RFile'

class AbstractPrinter:
    def __init__(self, name):
        self.name = name
        
    def printData(self, keys, keys_calculated, data):
        raise NotImplementedError
    
    def getName(self):
        return self.name
    



        

        
        
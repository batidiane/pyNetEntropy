from Utils import *
import IO
import socket
from statistics import frequency
class Data:
    keys_calculated = []
    printers = None
    
    def __init__(self, printnames):
        if Data.printers == None:
            Data.printers = []
            for n in printnames:
                Data.printers.append(load_printer(n))
        #elif type(Data.printer).__name__ != printname:
        #   Data.printer = load_printer(printname)
        self.data = {}
        
    
    def getData(self):
        return self.data
    
    def add(self, name, value):
        if name in self.data:
            self.data[name] += value
        else:
            self.data[name] = value
    def printData(self, keys):
        for n in Data.printers:
            n.printData(keys, Data.keys_calculated, self.data)

    def apply_function(self, keys, algorithm):
        for key in keys:
            try:
                new_key = key+'_'+algorithm.getName()+'_'+algorithm.getType()
                self.data[new_key] = algorithm.calculate(self.data[key])
                if new_key not in Data.keys_calculated:
                    Data.keys_calculated.append(new_key)
            except:
                pass



class IPPacket(Data):
    frequency_calculators = None
    def __init__(self, pktinfos, payload, timestamp):
        Data.__init__(self, ["graph","console"])
        self.add('timestamp', timestamp)
        for key in pktinfos:
            self.add(key, pktinfos[key])
        self.add('payload', payload)
        try:
            self.data['src_addr'] = socket.gethostbyaddr(self.data['src_addr'])
            self.data['dst_addr'] = socket.gethostbyaddr(self.data['dst_addr'])
        except:
            pass

    def apply_function(self, keys, algorithm):
        Data.apply_function(self, keys, algorithm)
        if IPPacket.frequency_calculators == None:
            IPPacket.frequency_calculators ={}
        for key in Data.keys_calculated:
            try:
                new_key = 'frequency_'+key
                entropy = self.data[key]
                timestamp = self.data['timestamp']
                if new_key not in IPPacket.frequency_calculators:
                    IPPacket.frequency_calculators[new_key] = frequency.Frequency()
                freq = IPPacket.frequency_calculators[new_key].calculate( timestamp, entropy)
                if freq != None:
                    self.data[new_key] = freq
            except:
                pass
        

        
    #def printData(self, keys):
        #Data.printer.printData(keys, Data.keys_calculated + IPPacket.frequency_calculators.keys(), self.data)
        #Data.printer.printData(keys, Data.keys_calculated, self.data)
        

        
def load_printer(printname):
    for mod_name in IO.__printers__:
        mod = __import__('IO.'+mod_name, fromlist=IO.__all__)
        for cl in dir(mod):
            try:
                print "classe="+cl
                mod_instance = getattr(mod, cl)()
                if mod_instance.getName() == printname:
                    print 'printname='+mod_instance.getName()
                    return mod_instance
            except Exception as e:
                pass
                #print e
        
    #return getattr(mod, IO.printers.default_printer_class)()

    


        
    

from IO.printers import AbstractPrinter

class RFile(AbstractPrinter):
    columns = None
    file = None
    def __init__(self):
        AbstractPrinter.__init__(self,"rfile")
        
    def printData(self, keys, keys_calculated, data):
        #Console.printData(self, keys, keys_calculated, data)
        
        if RFile.columns == None:
            RFile.columns = []
            RFile.file = open('data2.txt','a')
            res = ''
            for key in keys:
                if key not in RFile.columns:
                    RFile.columns.append(key)
                    res += key+'|'
            for key in keys_calculated:
                if key not in RFile.columns:
                    RFile.columns.append(key)
                    res += key+'|'
            res=res[:-1]
            RFile.file.write(res+'\n')
        res = ''
        for col in RFile.columns:
            try:
                res += str(data[col])+'|'
            except:
                res += '|'
        res=res[:-1]
        RFile.file.write(res+'\n')
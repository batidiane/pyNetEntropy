from IO.printers import AbstractPrinter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
import time

class Graph(AbstractPrinter):

    def __init__(self):
        AbstractPrinter.__init__(self, "graph")
        self.nb_print = 150
        self.tables = {}
        #self.lock = threading.Lock()
        #self.data = []
        #self.x=np.linspace(-5,5,100)
        #self.y=np.zeros((100,2))
        #self.y[:,0]=np.sin(self.x)
        #self.y[:,1]=np.cos(self.x)
        plt.ion()
        self.first = True
        #plt.plot(self.x)
        #plt.plot(self.y)
        #self.thread= threading.Thread(None, self.__thread, None)
        #plt.draw()
        #self.thread.start()
        
   
        
        
    def printData(self,keys, keys_calculated, data):
        timestamp = data['timestamp']
        #self.lock.acquire()
        plt.clf()
        for key in keys_calculated:
            try:
                
                #self.x.append(data['timestamp'])
                #self.data.append(data[key])
                #self.y.append(data[key])
                if key not in self.tables:
                    self.tables[key] = {}
                    self.tables[key]['ordonnee'] = []
                    self.tables[key]['abscisse'] = []
                #if not self.first:
                #        last_timestamp = self.tables[key]['abscisse'][len(self.tables[key]['abscisse'])-1]
                #        if (timestamp-last_timestamp) > 2:
                #            self.tables[key]['abscisse'].append(last_timestamp+0.1)
                #            self.tables[key]['ordonnee'].append(float(0.0))
                #            self.tables[key]['abscisse'].append(timestamp-0.1)
                #            self.tables[key]['ordonnee'].append(float(0.0))
                self.tables[key]['ordonnee'].append(data[key])
                self.tables[key]['abscisse'].append(timestamp)
                #table = self.tables[key][len(self.tables[key])-self.nb_print:len(self.tables[key])]
                #table =reduce_tab(self.tables[key]['ordonnee'], self.nb_print)
                #table2 = reduce_tab(self.tables[key]['abscisse'], self.nb_print)
                #temp = np.array(table)
                #temp2 = np.array(table2)
                #plt.plot(np.linspace(0,self.nb_print,len(table)),temp)
                t1,t2 = self.__calc_tabs(key)
                plt.plot(t2)
            except Exception as e:
                print e
        self.first = False
        plt.draw()
        #self.lock.release()
        #for key in self.tables:
        #    temp = np.array(self.tables[key])
        #    plt.plot(np.linspace(timestamp-5,timestamp+5,len(temp)), temp)
        #plt.draw()
        
    def __calc_tabs(self, key):
        table =reduce_tab(self.tables[key]['ordonnee'], self.nb_print)
        table2 = reduce_tab(self.tables[key]['abscisse'], self.nb_print)
        temp = np.array(table)
        temp2 = np.array(table2)
        return temp2, temp
    
    def __thread(self):
        try:
            while(1):
                time.sleep(0.5)
                #self.lock.acquire()
                plt.clf()
                for key in self.tables:
                    #self.tables[key][len(self.tables[key])-1] = float(0.0)
                    
                    self.tables[key]['ordonnee'].append(float(0.0))
                    max = self.tables[key]['abscisse'][len(self.tables[key]['abscisse'])-1]
                    self.tables[key]['abscisse'].append(max+0.5)
                    self.tables[key]['abscisse'].sort(cmp=None, key=None, reverse=False)    
                    temp2, temp = self.__calc_tabs(key)
                    #plt.plot(np.linspace(0,self.nb_print,len(table)),temp)
                    plt.plot(temp2,temp)
                plt.draw()
                #self.lock.release()
        except KeyboardInterrupt:
            self.thread.join()
            plt.close()
            raise KeyboardInterrupt
        
        
        
def reduce_tab(table, nb):
    
        return table[len(table)-nb:len(table)]
        
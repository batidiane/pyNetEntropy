import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from IO.printers import AbstractPrinter

class BarChart(AbstractPrinter):
    def __init__(self):
        AbstractPrinter.__init__(self, "bar")
        self.option = "src_port"
        self.labels = ()
        self.legends = ()
        self.bar = {}
        #plt.ion()
        #self.fig = plt.subplot(2,2,1)
        
        
        
    def printData(self,keys, keys_calculated, data):
        if data['src_port']<data['dst_port']:
            self.option = 'src_port'
        else:
            self.option = 'dst_port'
        #plt.clf()
        self.ax = plt.subplot2grid( (4,4), (0, 0), rowspan=4, colspan=2)
        rects = []
        k = data[self.option]
        if k not in self.bar:
            self.bar[k] = {}
            self.labels += (data[self.option], )
        nb_key = 0
        legends = ()
        for key in keys_calculated:
            nb_key += 1
            self.bar[k][key] = data[key]
            legends += (key, )
        N = len(self.bar)
        ind = np.arange(N)  # the x locations for the groups
        width = 0.35       # the width of the bars
        nb_key = 0
        legends2 = ()
        for key in keys_calculated:
            values = ()
            i = 0
            for b in self.bar:
                values += (self.bar[b][key], )
                
                i += 1
            if nb_key%2 == 0:
                rect = self.ax.bar(ind+width*float(nb_key) , values, width, color = 'r')
            else:
                rect = self.ax.bar(ind+width*float(nb_key) , values, width, color = 'y')
            nb_key += 1
            rects.append(rect)
            legends2 += (rect, )
        self.ax.legend(legends2, legends)
        labels = ()
        for b in self.bar:
            labels += (b, )
        #print labels
        self.ax.set_xticks(ind)
        self.ax.set_xticklabels(labels)
        
        for r in rects:
            autolabel(r, self.ax)
        #plt.draw()
            
            
def autolabel(rects, ax):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')
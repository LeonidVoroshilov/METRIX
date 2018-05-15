import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import time

import dataFunc as dF


def DrawGist(dictionary, isBar):
    
    dictionary = dF.ZNorm(dictionary)
    
    revDic = dict(zip(dictionary.values(), dictionary.keys()))
    matplotlib.style.use('ggplot')
    
    s = pd.Series(revDic)
    print(s)
    if(isBar):
        s.plot.hist(alpha=0.6)
    else:
        s.plot.kde()
        
    plt.savefig("D:\\WORK\\METRIX\\GRAPH\\" + str(time.time()) + ".png") 
    plt.clf()
    plt.cla()
    plt.close()    
    
def DrawComprGist( dicG, dicI, title):
    
    revDicG = dict(zip(dicG.values(), dicG.keys()))
    revDicI = dict(zip(dicI.values(), dicI.keys()))
    
    G = pd.Series(revDicG)
    I = pd.Series(revDicI)
    
    #G = pd.Series(dicI)
    #I = pd.Series(dicG)    
   
    
    G.plot.kde(color = "Green", title = "Density plot " + title)
    I.plot.kde(color = "Red")
    

    plt.savefig("D:\\WORK\\METRIX\\GRAPH\\" + str(time.time()) + ".png")   
    
    plt.clf()
    plt.cla()
    plt.close()      





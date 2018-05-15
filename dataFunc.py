import math

TRESHOLD = 100

def Normalize (dataVal):
    sum = 0
    for i in dataVal.keys():
        sum += dataVal[i]
    for i in dataVal.keys():
        dataVal[i] /= sum;
        
def ZNorm (dataVal):
    M = 0
    D = 0
    
    #Normalize(dataVal)
    
    for i in dataVal:
        M += float(i) * dataVal[i]
    
    for i in dataVal:
        D += dataVal[i] * ((i - M) ** 2)
        
    for i in dataVal:
        dataVal[i]  = (dataVal[i] - M) / D
        
    return dataVal
        
        
    
def procedeData (path):    
    file = open(path).read()    
    file = file.replace('.bmp', '').replace('\n', ' ').split(' ')
    
    data = {}    
    i = 0
    key1 = ""
    key2 = ""
    val = 0
        
    for  s in file:
        i = i + 1
        if i % 3 == 1: 
            key1 = s
        elif i % 3 == 2:
            key2 = s
        else:
            val = float(s)
            if key1 in data.keys():
                if key2 in data[key1].keys():
                    #print( "Warning! " + key1 + " " + key2 + " already exist")
                    continue
                else:
                    data[key1][key2] = {}                        
            else:
              data[key1] = {}
              data[key1][key2] = {}  

            data[key1][key2] = val
    
    return data


def isEquivalent (key1, key2):
    rawKey1 = key1.split('_')
    rawKey2 = key2.split('_')
    
    if (rawKey1[0] == rawKey2[0]):
        return True
    else: 
        return False
    
def GetNumbersFromSet(key, dataset, mode):
    dataVal = []
    
    for key1 in  dataset.keys():
        for key2 in dataset[key1].keys():
          if isEquivalent(key1, key) and isEquivalent(key2, key)  == mode :
            #print( key1 + " " + key2 + " " + str(dataset[key1][key2]))
            dataVal.append(round(dataset[key1][key2] * TRESHOLD) / TRESHOLD)
    
    return dataVal 

def CountFreq (dataVal):
    
    result = {}
    
    for val in dataVal:
        if val in result.keys():
            result[val] = result[val] + 1 
        else:
            result[val] = 1
    
    return result       
                
            
def GetAllNumbersFromSet( dataset, mode):
    dataVal = []
    
    for key1 in  dataset.keys():
        for key2 in dataset[key1].keys():
          if isEquivalent(key1, key2)  == mode :
            #print( key1 + " " + key2 + " " + str(dataset[key1][key2]))
            t = round(dataset[key1][key2] * TRESHOLD) / TRESHOLD
            #if (t < 0.6):
                #print( key1 + " " + key2 + " " + str(dataset[key1][key2]))
            dataVal.append(round(dataset[key1][key2] * TRESHOLD) / TRESHOLD)
    
    return dataVal  


    
    
    

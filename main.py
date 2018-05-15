import dataFunc as dF
import Graph as Gr
   

def main ():
    print("METRIX SYSTEM \nInput data file path:\n")
    #path = input()
    path = "D:\\WORK\\METRIX\\taylor.txt"
    #path = "D:\\WORK\\METRIX\\ifpp_qsw.txt"
    DataDic = dF.procedeData(path)
    
    
    #Testing 

    #print(dF.CountFreq(dF.GetAllNumbersFromSet(DataDic, True)))
    #Gr.DrawGist(dF.CountFreq(dF.GetAllNumbersFromSet(DataDic, True)), False)
#Gr.DrawGist(dF.CountFreq(dF.GetAllNumbersFromSet(DataDic, True)), True)
    #Gr.DrawComprGist(dF.ZNorm(dF.CountFreq(dF.GetNumbersFromSet("1", DataDic, True))), dF.ZNorm(dF.CountFreq(dF.GetNumbersFromSet("1", DataDic, False))), path + " key: 1Z")
    #Gr.DrawComprGist(dF.CountFreq(dF.GetNumbersFromSet("1", DataDic, True)), dF.CountFreq(dF.GetNumbersFromSet("1", DataDic, False)), path + " key: 1")
    
    Gr.DrawComprGist(dF.ZNorm(dF.CountFreq(dF.GetAllNumbersFromSet( DataDic, True))), dF.ZNorm(dF.CountFreq(dF.GetAllNumbersFromSet(DataDic, False))), path + " global")
    
    #Gr.DrawComprGist(dF.CountFreq(dF.GetNumbersFromSet("100", DataDic, True)), dF.CountFreq( dF.GetNumbersFromSet("100",DataDic, False)))
    
    path = "D:\\WORK\\METRIX\\ifpp_qsw.txt"
    DataDic = dF.procedeData(path)
    
    
    #Testing 

    print(dF.CountFreq(dF.GetNumbersFromSet("20", DataDic, True)))
    #Gr.DrawGist(dF.CountFreq(dF.GetAllNumbersFromSet(DataDic, True)), False)
#Gr.DrawGist(dF.CountFreq(dF.GetAllNumbersFromSet(DataDic, True)), True)
    #Gr.DrawComprGist(dF.ZNorm(dF.CountFreq(dF.GetNumbersFromSet("1", DataDic, True))), dF.ZNorm(dF.CountFreq(dF.GetNumbersFromSet("1", DataDic, False))), path + " key: 1Z")
    #Gr.DrawComprGist(dF.CountFreq(dF.GetNumbersFromSet("20", DataDic, True)), dF.CountFreq(dF.GetNumbersFromSet("20", DataDic, False)), path + " key: 1")
    
    Gr.DrawComprGist(dF.ZNorm(dF.CountFreq(dF.GetAllNumbersFromSet( DataDic, True))), dF.ZNorm(dF.CountFreq(dF.GetAllNumbersFromSet(DataDic, False))), path + " global")
    
    #Gr.DrawComprGist(dF.CountFreq(dF.GetNumbersFromSet("100", DataDic, True)), dF.CountFreq( dF.GetNumbersFromSet("100",DataDic, False)))
    
main()
    
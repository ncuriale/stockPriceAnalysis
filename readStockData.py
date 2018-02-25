import fix_yahoo_finance as yf
import numpy as np
import datetime

def getData(inData):
    
    #Get data download
    openData,num= getType(inData,'Open')
    highData,_= getType(inData,'High')
    lowData,_= getType(inData,'Low')
    closeData,_= getType(inData,'Close')    
    #adjCloseData,_= getType(inData,'Adj Close')
    #volumeData,_= getType(inData,'Volume')
    
    #Expand dimensions
    openData=np.expand_dims(openData, axis=0)
    highData=np.expand_dims(highData, axis=0)
    lowData=np.expand_dims(lowData, axis=0)
    closeData=np.expand_dims(closeData, axis=0)
    #adjCloseData=np.expand_dims(adjCloseData, axis=0)
    #volumeData=np.expand_dims(volumeData, axis=0)
    
    #Combine data array
    outData=np.vstack((openData,highData))
    outData=np.vstack((outData,lowData))
    outData=np.vstack((outData,closeData))
    #outData=np.vstack((outData,adjCloseData))
    #outData=np.vstack((outData,volumeData))
   
    ####outputs ( dataTypeIndex, stockIndex, dayIndex )
    
    return outData,num
    
def readStocks(stockNames,start,end,readIndx=0):        
    # Stocks to read in
    tickers=stockNames[0:readIndx]          
    # Stock data 
    out = yf.download(tickers,start,end,False)   
    return out
 
def getDate(inData):     
    dates=inData.index.values       
    dates=dates.reshape(len(dates),1)   
    
    #format dates 
    dates=formatDate(dates)     
          
    return dates, len(dates)

def formatDate(inData):  
    #make new array
    outData=[None] * len(inData)
    for i in range(len(inData)):
        outData[i]= datetime.datetime.utcfromtimestamp(inData[i].astype('O')/1e9)  
        
    return outData

def getType(inData,Type):     
    data=inData[[Type]].as_matrix()[:]
    outData,_= removeNaNs(data, len(data[0,:])) 
   
    num=len(outData[0,:])

    return outData, num

def getNames(inData):  
    temp= inData[['Open']].columns.values.tolist()
    nameData=[]
    for t in temp:
        nameData.append(t[1])
        
    data=inData[['Open']].as_matrix()[:]
    _,outData= removeNaNs(data, len(data[0,:]),nameData) 
    
    return outData
 
def removeNaNs(data,num,names=0):    
    out=[]
    nameOut=[]
    
    #go thru rest of stocks
    for i in range(0,num):                     
                
        nan=np.any(np.isnan(data[:,i]))
        if(nan==False):    
            if(len(out)==0):                
                out=np.array(data[:,i]).reshape(len(data[:,i]),1)
            else:
                add=np.array(data[:,i]).reshape(len(data[:,i]),1)
                out=np.hstack((out,add))
                
            if (not names==0): 
                nameOut.append(names[i])
        
    return out, nameOut 




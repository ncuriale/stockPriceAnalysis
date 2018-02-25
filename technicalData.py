import numpy as np
import talib

def setArrays(data,dates,indx,nData,days,deltaInc):

    #Initialize arrays
    sizeX=(nData,len(indx))
    sizeY=(nData,1)
    X=np.zeros(sizeX)
    Y=np.zeros(sizeY)
    
    #Daily Input Parameters  
    X=formX(data,indx,X)
    
    #Result based on future prices
    #Y=formY(data,X,Y,days,deltaInc)
    #Modify arrays to eliminate unneeded entries
    X,Y,modDates=modifyXY(X,Y,dates,indx,len(indx))
    
    #####test_trainSplit()
    
    return X,Y,modDates

def formX(data,indx,X):
    
    if (indx[0]):
        X[:,0] = data[0,:]#open
    if (indx[1]):
        X[:,1] = data[1,:]#high
    if (indx[2]):
        X[:,2] = data[2,:]#low
    if (indx[3]):
        X[:,3] = data[3,:]#close
    if (indx[4]):
        X[:,4] = 0#data[4,:]#adj close
    if (indx[5]):
        X[:,5] = 0#data[5,:]#volume
    if (indx[6]):
        X[:,6] = talib.RSI(data[3,:],timeperiod=14) #buy with low RSI <20-30 
    if (indx[7]):
        X[:,7] = talib.ROC(data[3,:], timeperiod=10)#better if increasing
    if (indx[8]):
        X[:,8] = 0#talib.OBV(data[4,:], data[5,:]) 
    if (indx[9]):
        X[:,9] = talib.BETA(data[1,:], data[2,:], timeperiod=5)
    if (indx[10]):
        X[:,10] = talib.STDDEV(data[3,:], timeperiod=5, nbdev=1)
    if (indx[11]):
        X[:,11] = talib.WILLR(data[1,:],data[2,:],data[3,:],timeperiod=40)  
    if (indx[12] and indx[13]):
        X[:,12],X[:,13] = talib.STOCH(data[1,:],data[2,:],data[3,:], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    if (indx[14] and indx[15] and indx[16]):
        X[:,14], X[:,15], X[:,16] = talib.MACD(data[3,:], fastperiod=12, slowperiod=26, signalperiod=10)
    if (indx[17]):#ROC of MACD
        for i in range(1,len(X)):            
            X[i,17] = X[i,16]-X[i-1,16]
    if (indx[18]):
        X[:,18] = talib.SMA(data[3,:], timeperiod=30) 
    if (indx[19]):
        X[:,19] = talib.SMA(data[3,:], timeperiod=60) #MAs mix with crossovers of price/other averages
    if (indx[20]):
        X[:,20] = talib.SMA(data[3,:], timeperiod=100) 
    if (indx[21]):
        X[:,21] = talib.SMA(X[:,11], timeperiod=30) 
    if (indx[22]):#ROC of WILLR
        for i in range(1,len(X)):            
            X[i,22] = X[i,21]-X[i-1,21]   
    if (indx[23] and indx[24]):#check of ROC of WILLR
        for i in range(1,len(X)):  
            if ( X[i-1,22]<0 and X[i,22]>0 ):          
                X[i,23] = 1  
            elif ( X[i-1,22]>0 and X[i,22]<0 ):          
                X[i,24] = 1   
    return X  

def formY(data,X,Y,days,deltaInc):  
            
    for i in range(0,len(data[0])-1):
        if((i+days)==len(X)):
            break
        
        #price difference over next "days"            
        delta = data[i+days,3]-data[i,3]      
        #price increase or decrease    
        if delta > deltaInc*data[i,3]:
            Y[i]=1
        else:
            Y[i]=0
        
    return Y  

def modifyXY(X,Y,dates,indx,numParam): 

    #Take out NaN rows
    sizetempX=(0,numParam)
    sizetempY=(0,1)
    tempX=np.empty(sizetempX)
    tempY=np.empty(sizetempY)
    tempDates=[]
    k=0
    for i in X: 
        if(np.all(np.isfinite(i))):
            tempX=np.vstack((tempX,i))
            tempY=np.vstack((tempY,Y[k]))
            tempDates.append(dates[k])
        k+=1 
    
    if(0):
        #Take out columns not included in indx
        for i in range(numParam,0,-1): 
            j=i-1
            if( not indx[j]):
                tempX=np.delete(tempX,j,1)    
    
    #ensure data set has even buy/sell values ---- may not be needed
    if(0):
        while(np.sum(tempY)!=int(0.5*len(tempY))):   
            k=0
            dFlag=1
            
            #if more sells
            if( np.sum(tempY)<int(0.5*len(tempY)) ):
                while(dFlag==1):
                    if(tempY[k]==0):
                        tempX=np.delete(tempX,k,0) 
                        tempY=np.delete(tempY,k,0)  
                        dFlag=0
                    else:
                        k+=1
             
            #if more buys   
            elif( np.sum(tempY)>int(0.5*len(tempY)) ):
                while(dFlag==1):
                    if(tempY[k]==1):
                        tempX=np.delete(tempX,k,0) 
                        tempY=np.delete(tempY,k,0)  
                        dFlag=0
                    else:
                        k+=1
                   
    return tempX,tempY,tempDates 
 
def test_trainSplit(X,Y,trainLength):
    
    trainLength=int(len(X)*0.75)
    testLength=len(X)-trainLength
    trainX = X[:trainLength,:] 
    trainY = Y[:trainLength,:] 
    testX = X[-testLength:,:] 
    testY = Y[-testLength:,:] 
       
    return trainX,trainY,testX,testY
    
    
    
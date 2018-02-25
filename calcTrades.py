
def calcBuys(X,dates):
    
    buyDates=[]
      
    for i in range(len(dates)):
        
        #check all buy rules for specific date
        res= buyRules(X[i,:])
        
        if (res):
            buyDates.append(dates[i])
                
    return buyDates

def calcSells(X,dates):
    
    sellDates=[]
      
    for i in range(len(dates)):
        
        #check all buy rules for specific date
        res= sellRules(X[i,:])
        
        if (res):
            sellDates.append(dates[i]) 

    return sellDates

def buyRules(X):          
    
    res=1
    
    #RSI
    if( not X[6]<30 ):
        res=0

    #WILLR
    if( not X[11]<-70 ):
        res=0

    #MACD1,  MACD2,  MACD3 
    if( not ( X[14]<0 and X[16]>0 )  ):
        res=0

    #SMA1,   SMA2,   SMA3 
    #if( not X[18]<X[19] ):
    #    res=0
    
    #check ROC of WILLR SMA
    #if( X[23]==0 ):
    #    res=0

    #stock price
    if( not ( X[3]>1.5 and X[3]<150 ) ):
        res=0
        
    return res


def sellRules(X):          
    
    res=1
    
    #RSI
    if( not X[6]>60 ):
        res=0

    #WILLR
    if( not X[11]>-30 ):
        res=0

    #MACD1,  MACD2,  MACD3 
    #if( not X[17]<-0.001 ):
    #    res=0

    #SMA1,   SMA2,   SMA3 
    #if( not X[18]>X[19] ):
    #    res=0
    
    #check ROC of WILLR SMA
    #if( X[24]==0 ):
    #    res=0

    #stock price
    if( not ( X[3]>1.5 and X[3]<150 ) ):
        res=0
            
    return res









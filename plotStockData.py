import matplotlib.pyplot as plt
import numpy as np

def plotData(data,dates,X,dates_X,buyDates,sellDates,stockName,iplot):
    #print (stockName) 
       
    #Plot dataframe 
    fig, ax1 = plt.subplots()   
    plt.figure(num=iplot)  
    plt1=plt.subplot(411)   
    fig.suptitle('Stocks over Time: '+stockName, fontsize=16)
    plt.plot(dates_X,X[:,3],c='k',label='Price') #price     
    plt.plot(dates_X,X[:,18],c='b',label='SMA1') #SMA1       
    plt.plot(dates_X,X[:,19],c='c',label='SMA2') #SMA1 
    #plt.plot(dates_X,X[:,20],c='m',label='SMA3') #SMA2
    plt1.set_ylabel('Value ($)', fontsize=12)  
    plt.ylim(0.95*np.min(data[:,3]),1.05*np.max(data[:,3])) 
    plt.legend(loc=2)         
    plt.grid()  
    for i in buyDates:
        plt.axvline(x=i, color='g', linestyle='-', label='buy')
    for i in sellDates:
        plt.axvline(x=i, color='r', linestyle='-', label='sell')
    
    plt2=plt.subplot(412)   
    plt2.set_ylabel('MACD', fontsize=12) 
    plt.plot(dates_X,X[:,14],c='b',label='MACD1') 
    plt.plot(dates_X,X[:,15],c='c',label='MACD2') 
    #plt.plot(dates_X,X[:,16],c='k',label='MACD3') 
    plt.bar(dates_X,X[:,16], 1, color='k', label='MACD3')
    plt.ylim(np.min(X[:,14])-0.5,np.max(X[:,14])+0.5)       
    plt.grid() 
    for i in buyDates:
        plt.axvline(x=i, color='g', linestyle='-', label='buy')
    for i in sellDates:
        plt.axvline(x=i, color='r', linestyle='-', label='sell')
    
    plt3=plt.subplot(413)   
    plt3.set_ylabel('RSI', fontsize=12) 
    plt.plot(dates_X,X[:,6],c='b',label='RSI') 
    #plt.plot(dates_X,X[:,23],c='b',label='RSI')
    #plt.plot(dates_X,X[:,24],c='r',label='RSI')
    plt.ylim(0,100)       
    plt.grid() 
    for i in buyDates:
        plt.axvline(x=i, color='g', linestyle='-', label='buy')
    for i in sellDates:
        plt.axvline(x=i, color='r', linestyle='-', label='sell')
     
    plt4=plt.subplot(414)   
    plt4.set_ylabel('WILLR%', fontsize=12) 
    plt.plot(dates_X,X[:,11],c='b',label='WILLR%') 
    plt.plot(dates_X,X[:,21],c='m',label='SMA') #SMA2
    plt.ylim(-100,0)       
    plt.grid() 
    for i in buyDates:
        plt.axvline(x=i, color='g', linestyle='-', label='buy')
    for i in sellDates:
        plt.axvline(x=i, color='r', linestyle='-', label='sell')         
    
    #plt3=plt.subplot(313)   
    #plt.plot(stockDates,X[:,5],c='c',label='Total Value') #price  
    #plt3.set_xlabel('Time (days)', fontsize=12)  
    #plt3.set_ylabel('WILLR%', fontsize=12) 
    #plt.plot((stockDates[0],stockDates[len(stockDates)-1]), (-20, -20), 'k--')
    #plt.plot((stockDates[0],stockDates[len(stockDates)-1]), (-50, -50), 'r--')
    #plt.plot((stockDates[0],stockDates[len(stockDates)-1]), (-80, -80), 'k--')
    #plt.ylim(-100,0)       
    #plt.grid() 
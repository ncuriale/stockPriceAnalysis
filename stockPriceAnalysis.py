###Imported packages
import pandas as pd 
import datetime
import numpy as np
import time
import tickerNames
from sklearn import ensemble
from matplotlib.pyplot import pause
import matplotlib.pyplot as plt

###User-defined files
import readStockData
import technicalData
import plotStockData
import calcTrades
import cryptoCurr

###########################################INPUTS##########################################

stockNames=tickerNames.names(5)     #Stock names
                                    
start_year=2017                     #Start year for stock info     
start_month=1                        #Start month for stock info
numStockPredict=len(stockNames)     #Number of stocks to analyze -- must be in order in stockNames array for multiPredictor

days=1
deltaInc=1.02

plotFlag=1                          #Flag to show plots or not
###########################################################################################

#    Select Indicators to compute ----- 1-Use 0-Not Use
#     Open,   High,   Low,   Close,  A.Close,   Vol,   
#     RSI,    ROC,    OBV,   BETA,   STDDEV,    WILLR,   
#     STOCH1, STOCH2, 
#     MACD1,  MACD2,  MACD3, ROC_MACD
#     SMA1,   SMA2,   SMA3

indx=[1,   1,   1,   1,   1,   1,   \
      1,   0,   0,   0,   0,   1,   \
      0,   0,   \
      1,   1,   1,   1,   \
      1,   1,   0,   \
      1,   1,   1,   1]

###########################################################################################

def main():
            
    # Start/end data 
    start = datetime.date(start_year,start_month,1)
    end = datetime.date.today() 
    duration = (end-start).days 
    buy_Date = end - datetime.timedelta(weeks=8)#datetime.date(2017,1,1)
    
    #read in stock data
    rawData= readStockData.readStocks(stockNames,start,end,numStockPredict) 
    #rawData = cryptoCurr.getQuandlData('XTSE/AZ')
    #rawData = cryptoCurr.getQuandlCrypto('BCHARTS/KRAKENUSD',"2016-12-06")
    
    stocks,nStocks= readStockData.getData(rawData)
    dates,nDays= readStockData.getDate(rawData)
    names= readStockData.getNames(rawData)
    
    j=0        
    #calculate technical indicators for each stock
    for i in range(0,nStocks):
        plot=0
        X,Y,dates_X= technicalData.setArrays(stocks[:,:,i],dates,indx,nDays,days,deltaInc)
           
        buyDates= calcTrades.calcBuys(X,dates_X)
        sellDates= calcTrades.calcSells(X,dates_X)
              
     #   for k in buyDates:
      #      if( buy_Date < k.date() ):
       #         plot=1
        plot=1      
        if( plot==1 ):
            j+=1
            print(names[i])               
            ##mark buys and sells w vertical lines
            plotStockData.plotData(stocks[:,:,i].T,dates,X,dates_X,buyDates,sellDates,names[i],j+1)
         
       
    #Show plots
    if(plotFlag==1):
        plt.show()
        input("Press Enter to continue...")
        plt.close('all')
       
if __name__ == "__main__":
    
    main()
    
    
    
import TSX
import NYSE
import NASDAQ
import USMF
import TSX_mod
import NYSE_mod
import TSX_new

def names(indx):
    
    if (indx==1):
        names=NYSE.NYSE()
    elif (indx==2):
        names=TSX.TSX()
    elif (indx==3):
        names=NASDAQ.NASDAQ()
    elif (indx==4):
        names=USMF.USMF()
    elif (indx==5):
        names=TSX_mod.TSX_mod()
    elif (indx==6):
        names=NYSE_mod.NYSE_mod()
    elif (indx==7):
        names=TSX_new.TSX_new()
        
    return names
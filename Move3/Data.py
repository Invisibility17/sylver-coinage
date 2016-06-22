class Data():
    def __init__( self, plays ):
        self.plays = plays

    def stringForFile(self):
        return """{0}\n{1}\n""".format( self.plays, self.whoWon() )

    def whoWon(self):
        if len(self.plays)%2 == 1:
            return "Player 1 lost."
        else:
            return "Player 1 won."

def greater( x, y, num=0):
    if x[num] > y[num]:
        return True
    elif y[num] > x[num]:
        return False
    elif len(x)-1 == num:
        return False
    elif len(y) -1 == num:
        return True
    else:
        return greater(x, y, num+1)  

def sortIt( dataList ):
    temp = [ dataList[0] ]
    for n in range(1, len(dataList), 1):
        for m in range(len(temp)):
            if dataList[n] not in temp:
                if greater( temp[m], dataList[n] ) == True:
                    temp.insert( m, dataList[n] )
                elif m==len(temp)-1:
                    temp.append( dataList[n] )

    return temp




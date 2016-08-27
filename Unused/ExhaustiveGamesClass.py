import collections
from NumericalSemigroupClass import NumericalSemigroup

def isDone( NS ):
        if [1,2,3] == NS.notInS:
            return True
        else:
            return False
        
def checker( NS ):
    
    if isDone( NS ) == True:
       
        return NS.gens
    else:
        results = []
        for n in NS.notInS:
            if n > 3:
                check = checker( NumericalSemigroup( NS.gens+[n]))

                if type(check[0]) == int:
                    
                    results.append(check)
                else:
                    results += check
        
        
        return results
    
class ExhaustiveGame():

    def __init__(self, P1):
        self.soulDict = collections.OrderedDict()
        self.P1 = P1
        self.index = []
        self.thirds = self.getThirds()
        
    def generateGamesPlural( self, nums, maximum=1000 ):
        nums.sort()
        for n in nums:
            if len(self.generateOneGame( n ) ) > maximum:
                print("Stopped generating after {0} because # of games was greater than {1}".format( n, maximum ) )
                break
        self.whichGamesGenerated()
        print()

    def storedNumGames(self):
        all = 0
        for n in self.soulDict:
            all += len( self.soulDict[n] )

        return all

    def whichGamesGenerated( self ):
        index = []
        for n in self.soulDict:
                index.append( n )
        self.index = sorted(index)
        return sorted(index)

    def getThirds(self):
        thirds = []
        for n in self.P1.notS:
                P2 = NumericalSemigroup( self.P1.gens + [n] )
                if P2.isIrreducible()==False and n > 3:
                        thirds.append( n )
        return thirds
        
    
    def generateOneGame(self, num):
        if num > 3:
            P2 = NumericalSemigroup( self.P1.gens + [num] )
            if P2.isIrreducible() == False:
                
                check = checker( P2 )
                self.soulDict[num] = check
                self.whichGamesGenerated()
                print("Generated {0} with {1} games".format( num, len(check)) )
                return check               
    
    def printAll(self):
        print("Printing all stored games")
        for n in self.index:
            self.printOne( n )

    def printList( self, nums):
        print("Printing list (in order): {}".format(nums) )
        for n in nums:
            self.printOne(n)

    def printOne(self, num ):
        maxl = 0
        for n in self.soulDict[num]:
            if len(n) > maxl:
                maxl = len(n)

        maxl = maxl // 2 + maxl%2
        print("Third play {}".format(num))
        print( "P1\tP2\t"*maxl)
        for n in self.soulDict[num]:
            print("\t".join( str(x) for x in n ) )
        print()



            

from NumericalSemigroupClass import NumericalSemigroup
from ReceiveGensFunctions import isGCD
from copy import deepcopy
class GameState():

    def __init__( self, plays ):
        assert 1==isGCD( plays ), "Initial 2 plays are not relatively prime"
        self.gameBoard = NumericalSemigroup( plays )
        self.plays = plays

    def makePlay( self, play ):
        assert play not in self.gameBoard.getInS(), "Invalid move; play already eliminated"
        self.plays.append( play )
        self.gameBoard = self.gameBoard.whatIfAddGens( self.plays )

    def getPlays( self ):
        return self.plays

    def getNextPlays( self ):
        return self.gameBoard.getNotInS()

    def getValidNextPlays( self ):
        thirds = []
        for n in self.gameBoard.getNotS():
                P2 = self.gameBoard.whatIfAddGens( [n] )
                if P2.isIrreducible()==False and n > 3:
                        thirds.append( n )
        return thirds

    def copy( self ):
        return GameState( deepcopy(self.plays) )
        
        


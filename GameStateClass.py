from NumericalSemigroupClass import NumericalSemigroup
from ReceiveGensFunctions import isGCD

class GameState():

    def __init__( self, play1, play2 ):
        assert 1==isGCD( [play1, play2] ), "Initial 2 plays are not relatively prime"
        self.gameBoard = NumericalSemigroup( [play1, play2] )
        self.plays = [play1, play2]

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
        copy = GameState( self.plays[0], self.plays[1] )
        for n in self.plays[2:]:
            copy.makePlay( n )
        return copy
        
    

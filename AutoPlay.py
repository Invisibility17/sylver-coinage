from GameStateClass import GameState
from ReceiveGensFunctions import *
from Data import sortIt
import pickle
import os.path

def main():
    good = load("good")
    bad = load("bad")
    trios = load("trios")

    while True:
        play(good, bad, trios)

def play(good, bad, trios):
    gens = receiveGens( True, [] )
    assert len(gens) == 2, "Starting with more than two plays: bad juju"
    game = GameState( gens )

    nPlays = game.getValidNextPlays()
   
    for play in nPlays:
        print( play, end = " ")
        
        k = checkIt( game.copy(), play, good, bad )
        if k==1:
            print( "We have found the good one!!!!", game.getPlays()+[play] )
    

    print("Good trios we've found:")
    for n in good:
        if (len(n) == 3) and (n not in trios):
            trios.append( n )
    
    trios = sortIt( trios )
    for n in trios:
        print( n, end = "\t" )

    save( good, "good" )
    save( bad, "bad" )
    save( trios, "trios")
    savetext( trios, "trios")

def checkIt( game, nextPlay, good, bad ):
    
    game.makePlay( nextPlay)
    nPlay = game.getValidNextPlays()
    counter = 0
    baseGens = game.gameBoard.getGens()
    if baseGens in good:
        return 1

    for n in nPlay:
        P1 = game.gameBoard.whatIfAddGens( [n] )
        gens = P1.getGens()

        if gens in good:
            bad.append( baseGens )
            return 0
        elif gens in bad:
            counter += 1
        elif P1.isIrreducible() == True:
            bad.append( gens )
            counter += 1
        else:
            x = checkIt( game.copy(), n, good, bad )
            if x==0:
                counter += 1
            elif x==1:
                bad.append( baseGens )
                return 0

    if counter == len( nPlay ):
        if baseGens not in good:
            good.append( baseGens )
            return 1

        
def savetext( data, name ):
    with open(name+".txt", "w") as filey:
        filey.write("If the smallest two numbers are not relatively prime, the multipicities will be wrong!\n")
        for n in data:
            strang = ""
            for m in n:
                strang += str( m )+" "

            mult = str((n[0]*n[1]-n[0]-n[1] -n[2])/n[0]) + " multiplicities from F(S)"
            filey.write( strang )
            filey.write( " "+mult )
            filey.write("\n")

    print("All trios saved to {}.txt!".format(name)) 
def save( listy, name ):
    pickle.dump( listy, open( name+".p", "wb"))

def load( name ):
    if os.path.isfile( name+".p"):
        return pickle.load( open( name+".p", "rb"))
    else:
        return []
    
if __name__ == '__main__':
    main()

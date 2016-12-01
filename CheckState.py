# py -3.4 C:\Python34\Scripts\build_exe.exe AutoPlay.py

from GameStateClass import GameState
from ReceiveGensFunctions import *
from Data import sortIt
from AutoPlay import *
import pickle
import os.path

def main():
    gens = receiveGens( True, [] )

    game = GameState( gens )
    checkState( game )

def checkState( game ):
    good = load("good")
    bad = load("bad")
    trios = load("trios")

    gens = game.getPlays()
    if gens in good:
        print("this situation is good for the person who just played: it's in the list.")
        return 0
    elif gens in bad:
        print("this situation is bad for the person who just played: it's in the list")
        return 0

    if game.gameBoard.isIrreducible():
        print( "this situation is bad for the person who just played: it's symmetrical")
        return 0
    
    k = checkIt( GameState( gens[1:] ), gens[0], good, bad)
    if k == 1:
        print("this situation is good for the person who just played. It's been added to the list.")
        save( good, "good" )
        save( bad, "bad" )
        return 0
    else:
        print("this situation is bad for the person who just played. It's been added to the list.")
        save( good, "good" )
        save( bad, "bad" )
        return 0

if __name__ == '__main__':
    while True:     main()

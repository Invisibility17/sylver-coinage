from NumericalSemigroupClass import NumericalSemigroup
from ExhaustiveGamesClass import ExhaustiveGame
from ReceiveGensFunctions import receiveGens
from Data import sortIt, Data
import pickle
import os.path

good = []
bad = []
trios = []

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
def checkit( situation ):
    #print("working...")
    sety = NumericalSemigroup( situation ).minGens
    #print( sety )
    nvect = ExhaustiveGame( NumericalSemigroup( situation )).thirds
    counter = 0
    
    if sety in good:
        return 1
    
    for n in nvect:
        
        P1 = NumericalSemigroup( sety + [n] )
        gens = P1.minGens
        
        if gens in good:
            bad.append( sety )
            return 0
        elif gens in bad:
            counter += 1
        elif P1.isIrreducible() == True:
            bad.append( gens )
            counter += 1
        else:
            x = checkit( sety+[n] )
            if x==0:
                counter += 1
            elif x==1:
                bad.append( sety )
                return 0

    if counter == len(nvect):
        if sety not in good:
            good.append( sety )
            return 1


def play():
    global good
    global bad
    global trios
    P1gens = NumericalSemigroup( receiveGens(True, [] ) ).minGens

    thirdly = ExhaustiveGame( NumericalSemigroup(P1gens )).thirds

    for n in thirdly:
        print( n, end = " ")
        k = checkit( P1gens+[n] )
        if k == 1:
            print("WE HAVE FOUND THE GOOD ONE!!!", P1gens+[n] )

    #print( "Good (after P1) sets", good)
    #print( "Bad (after P1) sets", bad)
    #print( good )
    print("Good trios we've found:")
    for n in good:
        if (len(n) == 3) and (n not in trios):
            trios.append( n )

    trios = sortIt( trios )
    #good = sortIt( good )
    #bad = sortIt( bad )
    for n in trios:
        print( n, end = "\t" )

    save( good, "good")
    save( bad, "bad")
    save( trios, "trios")
    savetext( trios, "trios")



good = load("good")
bad = load("bad")
trios = load("trios")
#print(good, bad, trios)
while True:
    play()
        


    


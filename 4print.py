# py -3.4 C:\Python34\Scripts\build_exe.exe 4print.py

import pickle
import os.path
from sys import exit
def main():
    good = load('good')
    bad = load('bad')
    included = getInput()
    print("Printing minimal generating sets which include 4 and {}".format(included))
    print("Good, for the person who has just played.")

    for val in good:
        if (len(val) == 4) and (val[0] == 4):
            p = True
            for x in included:
                if x not in val:
                    p = False
            if p: print( val )

    print("Bad, for the person who has just played")
    
    for val in bad:
        if (len(val) == 4) and (val[0] == 4):
            p = True
            for x in included:
                if x not in val:
                    p = False
            if p: print( val )

        
def getInput(  ):
    gens = input("Enter numbers you want in the quads (4 is assumed): ").split()
    if len(gens) > 0:
        if gens[0].lower() == "x":
            print("Bye!")
            exit()
        for n in range(len(gens)):
            gens[n] = int(gens[n])
        return gens
    return []
            
def load( name ):
    if os.path.isfile( name+".p"):
        return pickle.load( open( name+".p", "rb"))
    else:
        return []

while True: 
    main()



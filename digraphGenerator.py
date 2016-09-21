from ReceiveGensFunctions import receiveGens
from AssociatedSylverDigraphClass import AssociatedSylverDigraph


gens = receiveGens(0, [])

assert len( gens ) > 1

graph = AssociatedSylverDigraph( gens )

    
print( graph.getAssociatedSylverDigraph() )

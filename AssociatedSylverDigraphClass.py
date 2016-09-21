from NumericalSemigroupClass import NumericalSemigroup

class AssociatedSylverDigraph():

    def __init__(self, generators):
        NS = NumericalSemigroup( generators )

        self.nodes = NS.getNotS()[3:]
        self.hashFullGraph = {}
        for node in self.nodes:
            self.hashFullGraph[node] = []
            tempNS = NS.whatIfAddGens( [node] )
            
            extendedVals = tempNS.getInS()
            # Gets arcs even when they are larger than the new FS
            for val in range(max(tempNS.getInS()), max(NS.getNotS()), 1) : extendedVals.append( val )
            extendedVals = set( extendedVals )
            for dest in extendedVals:    
                if dest in NS.getNotS():
                    self.hashFullGraph[ node ] = self.hashFullGraph[node] + [dest]
            
        self.pairs = []
        for nodeOrigin in self.hashFullGraph:
            for nodeDest in self.hashFullGraph[ nodeOrigin ]:
                if not self.checkLongerPathExists( nodeOrigin, nodeDest ):
                    self.pairs.append( (nodeOrigin, nodeDest ) )

        
        
    def getAssociatedSylverDigraph( self ):
        return self.pairs

    def checkLongerPathExists( self, nodeOrigin, nodeDest ):
        if nodeOrigin == nodeDest : return False
        # This is a slightly modified breadth first search.
        toDo = self.hashFullGraph[ nodeOrigin ].copy()
        doneList = [nodeOrigin]
        toDo.remove( nodeOrigin )
        toDo.remove( nodeDest )


        while len(toDo) > 0:
            
            firstNode = toDo[0]
            toDo.remove( firstNode )
            
            doneList.append( firstNode )

            
            reachableNodes = self.hashFullGraph[ firstNode ]
            if nodeDest in reachableNodes:
                return True
            else:
                for node in reachableNodes:
                    if (node not in toDo) and (node not in doneList):
                        toDo.append( node )

        return False

    
                

        
        
    

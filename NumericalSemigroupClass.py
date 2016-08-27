FMAX = 800
class NumericalSemigroup():

    def __init__(self, generators):
        self.gens = self.getMinGenerators( generators )
        self.S = self.generateSemigroupDict()
        self.FS = self.Frobenius()
        self.inS = self.getInS()
        self.notInS = self.getNotS()

    
    def generateSemigroupDict( self ):
        """ Generates a dictionary which contains true if a number
            is in the numerical semigroup and false if not. """
        S={}

        for n in range(FMAX):
            S[n] = False
        for n in self.gens:
            S[n] = True
        S[0] = True

        while not self.ended(S):
            M = S.copy()
            for m in M:
                if S[m]  == True:
                    for n in range(len(self.gens)):
                        S[ m + self.gens[n] ] = True
        ep = self.endPoint(S)
        for n in S:
            if n > ep:
                S[n] = True

        return S

    def whatIfAddGens( self, newGens ):
        return NumericalSemigroup( self.gens + newGens  )



    def getGens( self ):
        return self.gens

    
    def Frobenius( self ):
        """ returns the Frobenius number """
        try:
            return max( self.getNotS())
        except:
            return 0

    def ended( self, S ):
        """ Tests whether we've reached F(S) """
        test = 0
        listS = []
        for n in S:
            if S[n] == True:
                listS.append(n)
        listS.sort()
        for n in listS: 
            for m in range(listS[1]):
                if n+m in listS:
                    test += 1
                if test == listS[1]:
                    return True   
            test = 0  
        return False

    def endPoint( self, S ):
        if type(S) == list:
            test = 0
            listS = []
            for n in S:
                if S[n] == True:
                    listS.append(n)
                    if self.ended(listS):
                        return max(listS)
        elif type(S) == dict:
            test = 0
            listS = []
            for n in S:
                if S[n] == True:
                    listS.append(n)
            listS.sort()
            for n in listS: 
                for m in range(listS[1]):
                    if n+m in listS:
                        test += 1
                    if test == listS[1]:
                        return n   
                test = 0

    def getInS( self ):
        """ Returns everything in S """
        ep = self.endPoint( self.S)
        self.inS = []
        for n in self.S:
            if self.S[n] and n <= ep:
                self.inS.append(n)

        self.inS.sort()
        return self.inS

    def getNotS( self ):
        """ Everything not in S """
        ep = self.endPoint( self.S)
        self.notS = []
        for n in self.S:
            if self.S[n] == False:
                self.notS.append( n )
        self.notS.sort()
        return self.notS
    
    def printS( self ):
        print( "In S:\n", self.getInS(), "and so on")

    def printNotS( self ):
        print( "Not in S:\n", self.getNotS() )

    def isIrreducible( self ):
        """ checks whether the semigroup is irreducible """
        if self.FS%2 == 0:
            if len(self.getNotS()) == self.FS/2:
                return True
        else:
            if len(self.getNotS()) == (self.FS+1)/2:
                return True
        return False
    
    def getApery( self ):
        """ returns apery set """
        apery = []
        mods = []
        if len(self.inS) > 1:
            for n in range(self.inS[1]):
                for m in self.inS:
                    if m%self.inS[1] not in mods:
                        mods.append(m%self.inS[1])
                        apery.append( m )
            apery.append( self.FS + self.inS[1] )
            apery.sort()
            self.apery = apery
            return apery
        else:
            self.apery = []
            return []

    def printApery( self ):
        print( "The Apery set is: {}".format( self.getApery() ))

    def getMinGenerators( self, tempGens ):
        
        tempGens.sort()
        minGens = []
        for n in range(len(tempGens)-1, 0, -1):
            if self.canLinearCombo( tempGens[n], tempGens[:n] )==False:
                minGens.append( tempGens[n] )
        minGens.append( tempGens[0] )
        minGens.sort()
        return minGens
        
    def printMinGens( self):
        print( "Minimum generators:", self.minGens )
        
    def canLinearCombo(self, maxy, nums ):
        """ Tests whether maxy is a linear combo of the numbers. Recursive! """
        if maxy >= 0:
            for n in nums:
                if maxy%n == 0:
                    return True
            for n in range(len(nums)):
                if self.canLinearCombo( maxy-nums[n], nums)==True:
                    return True
            return False
        else:
            return False

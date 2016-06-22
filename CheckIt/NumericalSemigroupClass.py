FMAX = 800
class NumericalSemigroup():

    def __init__(self, generators):
        self.gens = generators
        self.S = self.generateDict()
        self.FS = self.Frobenius()
        self.inS = self.getInS()
        self.notInS = self.getNotS()
        self.minGenerators()

    def generateDict( self ):
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

    def modifyDict( self ):
        
        M = self.S.copy()
        for m in M:
            if self.S[m] == True:
                for n in range(len(self.gens)):
                    self.S[m + self.gens[n]] = True

        ep = self.endPoint( self.S)
        for n in self.S:
            if n > ep:
                self.S[n] == True

        self.FS = self.Frobenius()

    def moreGens( self, generators ):
        for n in generators:
            self.gens.append( n )
        self.modifyDict()
        self.minGenerators()

    def Frobenius( self ):
        try:
            return max( self.getNotS())
        except:
            return 0

    def ended( self, S ):
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
        ep = self.endPoint( self.S)
        self.inS = []
        for n in self.S:
            if self.S[n] and n <= ep:
                self.inS.append(n)

        self.inS.sort()
        return self.inS

    def getNotS( self ):
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
        if self.FS%2 == 0:
            if len(self.getNotS()) == self.FS/2:
                return True
        else:
            if len(self.getNotS()) == (self.FS+1)/2:
                return True
        return False
    def getApery( self ):
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

    def whoWon( self ):
        if len(self.gens)%2 == 1:
            return "Player 1 loses."
        else:
            return "Player 1 wins."

    def minGenerators( self ):
        tempGens = self.gens.copy()
        tempGens.sort()
        minGens = []
        for n in range(len(tempGens)-1, 0, -1):
            if self.canLinearCombo( tempGens[n], tempGens[:n] )==False:
                minGens.append( tempGens[n] )
        minGens.append( tempGens[0] )
        minGens.sort()
        self.minGens = minGens.copy()
        
    def printMinGens( self):
        print( "Minimum generators:", self.minGens )
        
    def canLinearCombo(self, maxy, nums ):
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

    def goodChoice( self, k=2 ):
        self.getApery()
        choices = []
        plays = []
        for n in self.apery:
            plays.append( n-k*min(self.gens))
            if n - k*min(self.gens) < 0:
                choices.append( "Impossible")
            else:
                if n - k*min(self.gens) < 4:
                    if self.isIrreducible() == True:
                        if self.FS%2 == 1:
                            choices.append("Bad symmetric")
                        else:
                            choices.append("Bad pseudo")
                    else:
                        choices.append( "Bad, neither.")
                else:
                    lookgens = self.gens.copy()
                    lookgens.append( n - k*min(self.gens))
                    lookahead = NumericalSemigroup( lookgens )
                    if lookahead.isIrreducible( ) == True:
                        if self.FS%2 == 1:
                            choices.append( "Symmetric" )
                        else:
                            choices.append( "Pseudo")
                    else:
                        choices.append( "Neither")
                    
        return plays, choices

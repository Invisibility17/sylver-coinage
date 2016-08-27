"""
    def goodChoice( self, k=2 ):
        # tests whether a given move is a good play or no 
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
    """

    """
    def whoWon( self ):
        # Probably should move elsewhere 
        if len(self.gens)%2 == 1:
            return "Player 1 loses."
        else:
            return "Player 1 wins."
    """

    """               
    def modifyDict( self ):
        #WhY??? 
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
        # Edits the numerical semigroup 
        for n in generators:
            self.gens.append( n )
        self.modifyDict()
        self.minGenerators()
    """

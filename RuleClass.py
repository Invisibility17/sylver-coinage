class Rule( ):
    def __init__(self, ints, kind):
        assert len(ints) == 3
        self.E = ints[0]
        self.x = ints[1]
        assert ints[2]%2 == 1
        self.mod = ints[2]%8
        self.kind = kind

    def matches( self, gens ):
        if len(gens) != 4: return False
        if 4 not in gens: return False
        if E not in gens: return False
        odds = []
        for gen in gens:
            if gen%2 != 0:
                odds.append( gen )
        if len(odds) != 4:return False
        odds.sort()
        if odds[0]%8 != self.mod: return False
        if odds[1]-odds[0] != self.x: return False
        return True

    def getType( self ):
        return self.kind

    def isGood( self ):
        # Good for the last player to have played
        return self.kind.lower() == "good"

    def __str__( self ):
        return "<4, {0}, p, p+{1}>; p = {2} mod 8; {3} for the person who just played.".format( self.E, self.x, self.mod, self.kind)
    

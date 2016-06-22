def isOverlap( gens, inS):
    for n in range( len(gens)):
        if gens[n] in inS:
            return True
        
def receiveGens(initial, inS):
    gens = gensSequence(inS)
    while not isGCD1( gens ) and initial==True:
        gens += gensSequence(inS+gens)

    return gens

def gensSequence( inS ):
    gens = input("Enter generators separated by spaces (X to quit): ").split()
    if len(gens) > 0:
        if gens[0].lower() == "x":
            print("Bye!")
            exit()
        for n in range(len(gens)):
            gens[n] = int(gens[n])

        if isOverlap( gens, inS):
            print("Some of your choices are invalid! Please try again.")
            return gensSequence( inS )

        return gens
    else:
        return gensSequence( inS )

def isGCD( nums ):
    if len(nums)==1:
        return nums[0]
    elif len(nums) == 2:
        divisor = 1
        if 1 in nums:
            return divisor
        for n in range(2, min(nums)+1):
            if nums[0]%n ==0 and nums[1]%n == 0:
                divisor = n
        return divisor
    else:
        return isGCD( [nums[0], isGCD( nums[1:] )])

def isGCD1( nums ):
    return isGCD(nums)==1

#k = receiveGens( True, [] )

#print( k )

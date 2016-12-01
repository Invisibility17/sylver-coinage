from ReceiveGensFunctions import *
from AutoPlay import load, save
from RuleClass import Rule
from sys import exit


def main():
    print("Would you like to input rules or test a scenario?")
    message = """1: Input rules
2: Test scenario
3: Print rules.
>> """
    split = int(input(message))
    rules = load('rules')      
    if split == 1:
        print("Inputting rules...")
        
        while True:
            rule = receiveRule()
            rules.append( rule )
            cont = input("Continue? [y]/n ")
            save(rules, 'rules')
            if 'n' in cont.lower():
                exit()
        
    elif split == 2:
        scenario = receiveGens( True, [] )
        

        assert len(scenario) == 4, "Sorry, this only works for 4-generated game states."
    else:
        for rule in rules:
            print( rule )


def receiveRule():
    rules = load('rules')
    message = """Rules follow the form <4, E, p, p+x>, p = y mod 8 and can be good or bad.
E = 2 mod 4, and 6 <= E <= 2p-4.
p is an odd number greater than 3.
x = 2 mod 4, and 2 <= x <= E-4.
y = 1, 3, 5, or 7.
Please input E x and y in that order separated by spaces."""
    print(message)
    ruleInts = input(">> ").split()
    assert len(ruleInts)==3, "Oops, looks like you had too much or too little input!"
    for i in range(len(ruleInts)):
        ruleInts[i] = int(ruleInts[i])
    message = """Now, please input 1 or g for a rule that means the last player to play is in a winning situation.
    Input 2 or b for a rule that means the last player to play is in a losing situation."""
    print(message)
    ruleType = input(">> ")
    if ('g' in ruleType.lower()) or ('1' in ruleType): ruleType = 'good'
    else: ruleType == 'bad'
        

    return Rule( ruleInts, ruleType )
    

    

if __name__ == "__main__":
    main()

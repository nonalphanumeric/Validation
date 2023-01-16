from Rule import Rule

rule1 = Rule("r1",lambda c : c.aliceHere, a1)
rule2 = Rule("r2", lambda c : not c.aliceHere, a2)

def a1():

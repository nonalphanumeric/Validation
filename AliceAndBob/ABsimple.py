'''
Simple Alice and Bob exclusion.
Same idea as Hanoi
'''

from copy import deepcopy

from Misc.transitionRelation import TransitionRelation
from Soup.Rule import RuleAction
from Soup.SoupProgram import SoupProgram


class SoupABsimple(TransitionRelation):

    def guardAB(self, source, who, where):
        if where == "garden":
            if who == "alice":
                return not source[1]
            elif who == "bob":
                return not source[0]
        else:
            return True
    def executeAB(self, source, who, where):
        t = deepcopy(source)
        if who == "alice":
            t[0] = where == "garden"
        else:
            t[1] = where == "garden"
        return t


    def __init__(self):

        #How to represent the configuration in a simple manner ? let's just use a boolean each for Alice and Bob
        # Alice is the first and Bob the second, True if in garden, False if in house.
        self.program = SoupProgram([False,False])
        #What are the actions ? Each one can go to the garden or go to its house. But they can't go both in the garden at the same time.

        for who in ["alice", "bob"]:
            for where in ["garden", "house"]:
                rule_n = RuleAction(who + " goes to " + where,
                                    lambda source, who=who, where=where: self.guardAB(source, who, where),
                                    lambda source, who=who, where=where: self.executeAB(source, who, where))
                self.program.add(rule_n)


    def initialConf(self):
        return [self.program.ini]

    def enabledActions(self, source):
        return list(filter(lambda r: r.guard(source), self.program.rules))

    def execute(self, rule, source):
        t = rule.execute(source)
        return t


if __name__ == '__main__':
    soup = SoupABsimple()
    print(soup.initialConf())
    #print all rules
    for r in soup.program.rules:
        print(r)

    print(len(soup.enabledActions(soup.initialConf()[0])))

    new_conf = soup.execute(soup.program.rules[0], soup.initialConf()[0])
    print(new_conf)
    print(len(soup.enabledActions(new_conf[0])))



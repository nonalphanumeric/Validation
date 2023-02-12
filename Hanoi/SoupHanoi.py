'''
Same idea as SoupNBits but for Hanoi game
'''
from copy import deepcopy

from Misc.transitionRelation import TransitionRelation
from Soup.Rule import RuleAction
from Soup.SoupProgram import SoupProgram


class SoupHanoi(TransitionRelation):

    def guardHanoi(self, source, i, j):
        if len(source[i]) == 0:
            return False
        if len(source[j]) == 0:
            return True
        return source[i][-1] < source[j][-1]

    def executeHanoi(self, source, i, j):
        # we need to perform on a copy of the source using deepcopy
        t = deepcopy(source)

        # we need to move the top disk of i to j
        t[j].append(t[i].pop())

        # we return the new configuration
        return t

    def __init__(self, n):
        self.n = n
        self.program = SoupProgram([[1, 2, 3], [], []])
        # What are the actions ?
        # We can move a disk from a tower to another tower, lets say from i to j.
        # What are the guards ?
        # We can move a disk from i to j if the top disk of i is smaller than the top disk of j.
        # So, as guards, we will have to check if the top disk of i is smaller than the top disk of j.
        # Also we need the check if the tower i is not empty.
        # Let's implement a method above for that thing

        for i in range(n):
            for j in range(n):
                if i != j:  # Let's start simple and not allow to move a disk to the same tower
                    rule_n = RuleAction("Move disk from " + str(i) + " to " + str(j),
                                        lambda source, i=i, j=j: self.guardHanoi(source, i, j),
                                        lambda source, i=i, j=j: self.executeHanoi(source, i, j))
                    self.program.add(rule_n)

    def initialConf(self):
        return [self.program.ini]

    def enabledActions(self, source):
        return list(filter(lambda r: r.guard(source), self.program.rules))

    def execute(self, rule, source):
        t = rule.execute(source)
        return [t]


if __name__ == '__main__':
    soup = SoupHanoi(3)
    print(soup.initialConf())

    print("Here is a list of all rules as references: ")
    for rule in soup.program.rules:
        print(rule)

    print("\n\n")
    for rule in soup.enabledActions([[1, 2, 3], [], []]):
        print(str(rule) + " is enabled")
        for res in soup.execute(rule, [[1, 2, 3], [], []]):
            print(res)

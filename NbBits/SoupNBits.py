'''
What do we want ?
In this class, we are going to have a SoupProgram with a list of rules.
Remember, rules are transition, the guards tells us if the transition is enabled for the source or not.
The class for rules is RuleAction, which also contains an action.

Basically, from a config, we will see the list of enabled actions and then execute them to get the next configs.
This action can also perform some other things if need be, but in the case of NBits, their won't be any.

'''
import copy

from Soup.Rule import RuleAction
from Soup.SoupProgram import SoupProgram


class SoupNBits:


    def __init__(self, n):
        self.n = n
        self.program = SoupProgram([0])
        for i in range(n):

            # We create a rule for each bit. Guard is always true, action is to flip the bit
            rule_n = RuleAction("Flip bit " + str(i), lambda source: True, lambda source, i=i: source ^ (1 << i))

            self.program.add(rule_n)

    def initialConf(self):
        return [0]

    def enabledActions(self, source):
        return list(filter(lambda r: r.guard(source), self.program.rules))

    def execute(self, rule, source):
        t = rule.execute(source)
        return t

    def print_as_binary(self, res):
        print(format(res, '#0{}b'.format(self.n + 2)))

if __name__ == "__main__":
    soup = SoupNBits()
    for res in soup.initialConf():
        soup.print_as_binary(res)
    for rule in soup.enabledActions(0):
        print(str(rule) + " is enabled")
        for res in soup.execute(rule, 0):
            soup.print_as_binary(res)






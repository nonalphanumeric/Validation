from copy import deepcopy

from AliceAndBob.ABsimple import SoupABsimple
from Soup.Rule import RuleAction
from Soup.SoupProgram import SoupProgram


class SoupABflag():
    def __init__(self):
        self.program = SoupProgram([("house", False), ("house", False)])

        for i, name in enumerate(["alice", "bob"]):
            for state in ["house", "waiting", "garden"]:
                rule_name = f"{name} goes to {state}"
                guard = lambda source, i=i, state=state: self.guard(source, i, state)
                action = lambda source, i=i, state=state: self.action(source, i, state)
                self.program.add(RuleAction(rule_name, guard, action))

    def guard(self, source, i, state):
        source=source[0]
        other = (i + 1) % 2
        if state == "house":
            #Can only go to house if was in garden or, for bob only, if was waiting (avoid the deadlock)
            return source[i][0] == "garden" or (i == 1 and source[i][0] == "waiting")
        elif state == "waiting":
            #only if was in house
            return source[i][0] == "house"
        elif state == "garden":
            return source[i][0] == "waiting" and not source[other][1]

    def action(self, source, i, state):
        source = source[0]
        t = deepcopy(source)
        if state == "waiting":
            t[i] = (state, True)
        elif state == "garden":
            t[i] = (state, True)
        else:
            t[i] = (state, False)
        return t

    def initialConf(self):
        return [self.program.ini]

    def enabledActions(self, source):
        return list(filter(lambda r: r.guard(source), self.program.rules))

    def execute(self, rule, source):
        t = rule.execute(source)
        return t

    def explore_configurations(self,current_conf, max_depth, depth=0):
        for r in self.enabledActions(current_conf):
            indent = "\t" * depth
            print(f"{indent}Doing the enabled action: {r.name}")
            new_conf = self.execute(r, current_conf)
            print(f"{indent}{str(new_conf)}")
            if depth < max_depth:
                self.explore_configurations( new_conf, max_depth, depth + 1)

if __name__ == "__main__":
    soup = SoupABflag()
    initial = soup.initialConf()
    print(soup.initialConf())
    '''
    #execute a rule
    for r in soup.enabledActions(initial): #C'est brute de décoffrage mais là faut vraiment voir ce qu'il se passe
        print("\tDoing the enabled action : " + r.name)
        new_conf = soup.execute(r, initial)
        print("\t" + str(new_conf))
        for r2 in soup.enabledActions(new_conf):
            print("\t\tDoing the enabled action: " + r2.name)
            new_conf2= soup.execute(r2, new_conf)
            print("\t\t" + str(new_conf2))
            for r3 in soup.enabledActions(new_conf2):
                print("\t\t\tDoing the enabled action: " + r3.name)
                new_conf3 = soup.execute(r3, new_conf2)
                print("\t\t\t" + str(new_conf3))
                for r4 in soup.enabledActions(new_conf3):
                    print("\t\t\t\tDoing the enabled action: " + r4.name)
                    new_conf4 = soup.execute(r4, new_conf3)
                    print("\t\t\t\t" + str(new_conf4))
    '''


    #gotta love recursion
    soup.explore_configurations(initial, 5)





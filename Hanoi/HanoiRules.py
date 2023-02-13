from copy import deepcopy

from Misc.transitionRelation import TransitionRelation


class HanoiRules(TransitionRelation):

    def __init__(self):
        self.initial = [[1,2,3], [], []]

    def next(self, source):
        # from a source configuration, compute all possibles next configurations
        all_config = []
        for i in range(3):
            for j in range(3):
                if i != j:
                    if len(source[i]) == 0:
                        continue
                    if len(source[j]) == 0 or source[i][-1] < source[j][-1]:
                        config = deepcopy(source)
                        config[j].append(config[i].pop())
                        all_config.append(config)
        return all_config


    def roots(self):
        return self.initial


if __name__ == '__main__':
    hanoi = HanoiRules()
    print(hanoi.roots())
    for res in hanoi.next(hanoi.roots()):
        print("\t" + str(res))
        for res2 in hanoi.next(res):
            print("\t"*2 + str(res2))


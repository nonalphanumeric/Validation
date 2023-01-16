from copy import deepcopy, copy

from transitionRelation import TransitionRelation


class HanoiRules(TransitionRelation):

    def __init__(self):
        self.initial = [[1,2,3], [], []]

    def next(self, source):
        # from a source configuration, compute all possibles next configurations
        all_config = []
        for i in range(0, 3):
            for j in range(0, 3):
                config = deepcopy(source)
                if i != j:
                    if len(config[i]) != 0:
                        if len(config[j]) == 0:
                            config[j].insert(0, config[i].pop(0))
                            all_config.append(config)
                        elif config[i][len(config[i]) - 1] < config[j][len(config[j]) - 1]:
                            config[j].insert(0,config[i].pop(0))
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


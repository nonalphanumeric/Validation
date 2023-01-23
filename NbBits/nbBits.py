from copy import deepcopy

from Misc.transitionRelation import TransitionRelation


class NbBits(TransitionRelation):
    def flipnthbit(self, n, k):
        return n ^ (1 << k)

    def roots(self):
        return 0

    def next(self, source):
        result = []
        for i in range(0, self.k):
            candidate = deepcopy(source)
            candidate = self.flipnthbit(candidate, i)
            result.append(candidate)
        return result

    def __init__(self, k):
        self.k = k


# main
if __name__ == '__main__':
    k = 6
    nb = NbBits(k)
    for res in nb.next(nb.roots()):
        print(format(res, '#0{}b'.format(k + 2)))
        for res2 in nb.next(res):
            print("\t" + format(res2, '#0{}b'.format(k + 2)))


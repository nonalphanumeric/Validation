from identityProxy import IdentityProxy
from HanoiConfig import HanoiConfig


class ParentTraceProxy(IdentityProxy):
    def __init__(self, operand, dict):

        super().__init__(operand)
        self.dict = dict

    def roots(self):
        neighbours = self.operand.roots()
        for n in neighbours:
            self.dict[n] = n
        return neighbours

    def next(self, source):
        neighbours = self.operand.next(source)
        for n in neighbours:
            if n not in self.dict:
                self.dict[n] = source
        return neighbours

    def get_trace(dic, target):
        result, tmp = dict(target)
        if result:
            trace = []
            initial = target.initial()[0]
            while tmp != initial:
                trace.append(tmp)
                tmp = target.parents[tmp]
            trace.append(initial)
            trace.reverse()
            return trace


if __name__ == '__main__':
    h = HanoiConfig(3,3)
    pDict = {}
    ptp = ParentTraceProxy(h, pDict)


import inspect

from identityProxy import IdentityProxy
from Hanoi.HanoiConfig import HanoiConfig
from Misc.Traversal import predicate_finder

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

    def get_trace(self, dict,target):
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

    def predicate(self,transition_relation, predicate):
        print(f'{"-" * 50}\npredicate model-checking for:\n{inspect.getsource(predicate)}')

        parentTP = ParentTraceProxy(transition_relation)

        [pred, found, count, target], known = predicate_finder(parentTP, predicate)

        trace = []
        if found is True:
            trace = self.get_trace(parentTP.parents, target, parentTP.roots())
            trace_string = f'\n{"-" * 20}\n'.join(str(x) for x in trace)
            print(f'The trace is: \n{trace_string}')


if __name__ == '__main__':
    h = HanoiConfig(3,3)
    pDict = {}
    ptp = ParentTraceProxy(h, pDict)
   

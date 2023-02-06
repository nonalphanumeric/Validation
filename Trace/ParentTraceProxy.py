import inspect

from Misc.DicGraph import DicGraph
from identityProxy import IdentityProxy
from Hanoi.HanoiConfig import HanoiConfig
from Misc.Traversal import predicate_finder, bfs


class ParentTraceProxy(IdentityProxy):
    def __init__(self, operand, dict):
        super().__init__(operand)
        self.dict = dict

    def roots(self):
        #Copie les entités de TransitionRelation dans dict et retourne les EntryPoints
        neighbours = self.operand.getEntry()
        for n in neighbours:
            self.dict[n] = n
        return neighbours

    def next(self, source):
        #Retourne les entités suivantes de source et effectue aussi une copie de la TransitionRelation dans dict
        #des éléments qui ne sont éventuellement pas déjà dans dict.
        neighbours = self.operand.next(source)
        for n in neighbours:
            if n not in self.dict:
                self.dict[n] = source
        return neighbours

    def get_trace(self,dic, target):
        res = [target] #trace sera la liste res
        courant = target
        print("Courant = " + str(courant) + ", dic[courant] = " + str(dic[courant]))
        while courant != dic[courant] :
            courant = dic[res[-1]] #le dernier de la trace
            res.append(courant)
        return res


if __name__ == '__main__':

    dic = {0: [1,2], 1: [3,4], 2: [5,6], 3: [], 4: [], 5: [], 6: []}
    graph = DicGraph(dic, [0])
    ptp = ParentTraceProxy(graph, {})

    print(ptp.get_trace(dic, 6))

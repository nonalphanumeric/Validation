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
        #Attention, ne retourne qu'une trace pour le moment (en passant par le premier parent)
        res = [target] #trace sera la liste res
        courant = target

        #On remonte la trace en utilisant le dictionnaire reverse jusqu'à arriver à un élément qui n'a pas de parent
        revdic=self.reverse_graph(dic)
        #tant que courant a un parent
        while revdic[courant]:
            #on ajoute le parent à la trace
            res.append(revdic[courant][0])
            #on passe au parent
            courant = revdic[courant][0]
        return res


    def reverse_graph(self, dic):
        #dic est de la forme (entité, [entités enfants])
        #retourne un dictionnaire de la forme (entité, [entités parents])
        #add the entrypoints

        res = {}
        for k in dic:
            res[k] = []
        for k in dic:
            for v in dic[k]:
                if v not in res:
                    res[v] = [k]
                else:
                    res[v].append(k)
        return res




if __name__ == '__main__':

    dic = {0: [1,2], 1: [3,4], 2: [5,6], 3: [], 4: [], 5: [], 6: []}
    graph = DicGraph(dic, [0])
    print(graph.graph)
    ptp = ParentTraceProxy(graph, {})
    print(ptp.reverse_graph(dic))

    print(ptp.get_trace(dic, 6))
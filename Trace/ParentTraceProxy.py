
from Misc.DicGraph import DicGraph
from Trace.identityProxy import IdentityProxy


class ParentTraceProxy(IdentityProxy):
    def __init__(self, operand, dict):
        super().__init__(operand)
        self.dict = dict

    def roots(self):
        """
        Copies the entities of the TransitionRelation into dict and returns the EntryPoints.
        """
        neighbours = self.operand.getEntry()
        for n in neighbours:
            self.dict[n] = n
        return neighbours

    def next(self, source):
        """
        Returns the next entities from source and also copies the TransitionRelation into dict
        for elements that are not already in dict.
        """
        neighbours = self.operand.next(source)
        for n in neighbours:
            if n not in self.dict:
                self.dict[n] = source
        return neighbours

    def get_trace(self,dic, target):
        """
        Returns one trace for the moment (by passing through the first parent).
        """
        res = [target] #trace is the res list
        current = target

        #We go up the trace using the reverse dictionary until we reach an element that has no parent.
        revdic=self.reverse_graph(dic)
        #while current has a parent
        while revdic[current]:
            #add the parent to the trace
            res.append(revdic[current][0])
            #go to the parent
            current = revdic[current][0]
            #Danger, if we have a cycle, we risk looping indefinitely, not a great fix, but it should do:
            #if the parent is an entrypoint, stop.
            if current in self.operand.roots():
                break
        return res

    def get_traces(self, dic, target, path=None, all_paths=None):
        """
        Returns all traces using recursion.
        """
        if path is None:
            path = []
        if all_paths is None:
            all_paths = []

        path.append(target)
        revdic = self.reverse_graph(dic)

        if revdic[target]: #check if it has at least a parent
            for parent in revdic[target]: #recursion on all parents
                self.get_traces(dic, parent, path.copy(), all_paths)
        else: #if it has no parent, we have a trace, TODO: modify for stopping at entrypoints
            all_paths.append(path)

        return all_paths



    def reverse_graph(self, dic):
        """
        This function takes a dictionary `dic` in the form (entity, [child entities])
        and returns a dictionary in the form (entity, [parent entities]).

        :param dic: dictionary with entity as key and list of child entities as value
        :type dic: dict

        :returns: dictionary with entity as key and list of parent entities as value
        :rtype: dict
        """
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
    print(ptp.get_traces(dic, 6))

    #lets generate a new graph with some nodes that have multiples parents
    dic = {0: [1,2,7,8], 1: [3,4], 2: [5,6], 3: [], 4: [], 5: [], 6: [], 7: [5,6], 8: [5,6]}

    graph = DicGraph(dic, [0])
    ptp = ParentTraceProxy(graph, {})
    print(ptp.get_trace(dic, 6))
    print(ptp.get_traces(dic, 6)) #IT WORKSSSSSSSSSSS !!! I'M A GENIOUS !!!!!!$


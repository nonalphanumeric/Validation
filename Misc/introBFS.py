from collections import deque

'''
/!\ TO BE SCRAPED /!\
Most of the work will be transfered to DicGraph.py and this file will be deleted as part of a rework/overhaul
'''
class Graph(dict):
    def __init__(self):
        self.initial = None

    def add(self, a, neighbours, initial=False):
        self[a] = neighbours
        if initial:
            assert self.initial == None
            self.initial = self[a]

    def get(self, a):
        return self[a]

    def get_initial(self):
        return self.initial


def bfs(graph, o, on_entry=lambda source, n, o: None,
        on_known=lambda source, n, o: None,
        on_exit=lambda source, o: None):
    knowns = set()
    frontier = deque()
    at_start = True
    while frontier or at_start:
        source = None
        if at_start:
            neighbours = graph.get_initial()
            at_start = False
        else:
            source = frontier.popleft()
            neighbours = graph.get(source)
        for n in neighbours:
            if n in knowns:
                on_known(source, n, o)
                continue
            else :
                on_entry(source, n, o)  # on decouvre un voisin
                knowns.add(n)
                frontier.append(n)
    on_exit(source, o)
    return knowns


if __name__ == "__main__":
    graph = Graph()
    pere = "a"
    enfants = ["b", "c", "d"]
    enfants_b = ["e", "f"]
    enfants_c = ["r", "t"]

    graph.add("a", enfants, initial=True)
    graph.add("b", enfants_b)
    graph.add("c", enfants_c)
    graph.add("d", [])
    graph.add("e", [])
    graph.add("f", ["f"])
    graph.add("r", [])
    graph.add("t", ["a"])


    def basic1(source, n, o):
        if n is o:
            print("target trouvée : %s" % n)


    def basic2(source, n,o):
        if n is o:
            print("target trouvée mais onknown")


    def nothing1(source, n, o):
        pass


    def nothing2(source, o):
        pass

    def search_predicate(source,n, o):
        pass

    o = "f"
    bfs(graph, o, basic1, basic2, nothing2)





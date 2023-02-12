from collections import deque

from Misc.transitionRelation import TransitionRelation


class DicGraph(TransitionRelation):
    '''
    A graph represented as a dictionary.
    Exemples:
    dico = {0: [1,2], 1: [3,4], 2: [5,6], 3: [], 4: [], 5: [], 6: []}
    Represent the following graph:
        0
      |   \
     1     2
    | \   | \
    3 4   5 6
    '''
    def __init__(self, dico, roots):
        self.graph = dico  # dico a utiliser
        self.entrypoints = roots  # les points d'entree

    def roots(self):
        return self.entrypoints

    def next(self, source):
        try:
            return self.graph[source]
        except KeyError:
            return []



    '''
    bfs = Breadth First Search
    Allows for a breadth first search on a graph represented as a dictionary.
    Uses a queue to store the nodes to visit and a set to store the nodes already visited.
    Uses three lambda functions to specify what to do when a node is visited i.e. on_entry, 
    when a node is already known, i.e. on_known and when the search is finished i.e. on_exit.
    The lambda functions are called with the following parameters:
    - source: the node from which the current node was discovered
    - n: the current node
    - acc: the accumulator
    '''

    def bfs(self, acc, on_entry=lambda source, n, acc: None,
        on_known=lambda source, n, acc: None,
        on_exit=lambda source, acc: None):

        knowns = set()
        frontier = deque()
        at_start = True
        while frontier or at_start:
            source = None
            if at_start:
                neighbours = self.roots()
                at_start = False
            else:
                source = frontier.popleft()
                neighbours = self.next(source)
            for n in neighbours:
                if n in knowns:
                    on_known(source, n, acc)
                    continue
                else :
                    on_entry(source, n, acc)
                    knowns.add(n)
                    frontier.append(n)
        on_exit(source, acc)
        return knowns

    '''
    Using bfs, this function allows for predicate finding.'''

    def predicate_finder(self, predicate=lambda n: False):
        #create the accumulator which contains a boolean if the predicate is true at least once, and the list
        #nodes for which the predicate is true
        accumulator = [False, []]

        def check_predicate(s, n, a):

            # check predicate, if true, append the node to the accumulator
            if predicate(n):
                a[0] = True
                a[1].append(n)

        self.bfs(accumulator, on_entry=check_predicate)
        return accumulator






    


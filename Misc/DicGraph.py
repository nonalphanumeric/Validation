from collections import deque

from Misc.transitionRelation import TransitionRelation


class DicGraph(TransitionRelation):
    """
    A graph represented as a dictionary.
    Examples:
    dico = {0: [1,2], 1: [3,4], 2: [5,6], 3: [], 4: [], 5: [], 6: []}
    Represents the following graph:
        0
      |   \
     1     2
    | \   | \
    3 4   5 6
    """
    def __init__(self, dico, roots):
        """
        Initialize the graph with the given dictionary and roots.
        """
        self.graph = dico
        self.entrypoints = roots

    def roots(self):
        """
        Return the entry points of the graph.
        """
        return self.entrypoints

    def next(self, source):
        """
        Return the neighbors of the given source node.
        """
        try:
            return self.graph[source]
        except KeyError:
            return []

    def bfs(self, acc, on_entry=lambda source, n, acc: None,
        on_known=lambda source, n, acc: None,
        on_exit=lambda source, acc: None):
        """
        Perform a breadth-first search on the graph represented as a dictionary.

        The search uses a queue to store the nodes to visit and a set to store
        the nodes already visited. The function uses three lambda functions
        to specify what to do when a node is visited (`on_entry`), when a node
        is already known (`on_known`), and when the search is finished (`on_exit`).

        The lambda functions are called with the following parameters:
        - `source`: the node from which the current node was discovered
        - `n`: the current node
        - `acc`: the accumulator

        Returns:
        A set of the known nodes.
        """
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

    def predicate_finder(self, predicate=lambda n: False):
        """
        Find a node in the graph that satisfies the given predicate.

        The function uses the `bfs` method to perform the search and calls
        the `predicate` function for each node visited to check if it
        satisfies the given condition.

        Returns:
        A list containing a boolean indicating whether the predicate is true
        for at least one node and a list of nodes for which the predicate is true.
        """
        accumulator = [False, []]

        def check_predicate(s, n, a):

            # check predicate, if true, append the node to the accumulator
            if predicate(n):
                a[0] = True
                a[1].append(n)

        self.bfs(accumulator, on_entry=check_predicate)
        return accumulator








    


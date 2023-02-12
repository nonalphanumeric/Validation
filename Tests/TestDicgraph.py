import unittest
from Misc.DicGraph import DicGraph
from Trace import ParentTraceProxy

def generate_graph():
    dico = {0: [1, 2], 1: [3, 4], 2: [5, 6], 3: [], 4: [], 5: [], 6: []}
    roots = [0]
    return DicGraph(dico, roots)


def generate_graph_with_loop():
    '''generate a graph with a loop'''
    dico = {0: [1, 2], 1: [3, 4], 2: [5, 6], 3: [], 4: [], 5: [], 6: [0]}
    roots = [0]
    return DicGraph(dico, roots)


def generate_graph_with_two_roots():
    dico = {0: [1, 2], 1: [3, 4], 2: [5, 6], 3: [], 4: [], 5: [], 6: []}
    roots = [0, 2]
    return DicGraph(dico, roots)

def generate_complex_graph():
    #should have multiple roots, and cases of nodes with multiple parents
    dico = {0: [1, 2, 7, 8], 1: [3, 4], 2: [5, 6], 3: [], 4: [], 5: [], 6: [], 7: [5, 6], 8: [5, 6]}
    roots = [0, 1]
    return DicGraph(dico, roots)


class TestDicGraph(unittest.TestCase):
    def test_simple_graph(self):
        graph = generate_graph()
        self.assertEqual(graph.roots(), [0])
        self.assertEqual(graph.next(0), [1, 2])
        self.assertEqual(graph.next(1), [3, 4])
        self.assertEqual(graph.next(2), [5, 6])
        self.assertEqual(graph.next(3), [])
        self.assertEqual(graph.next(4), [])
        self.assertEqual(graph.next(5), [])
        self.assertEqual(graph.next(6), [])

    def test_graph_with_loop(self):
        graph = generate_graph_with_loop()
        self.assertEqual(graph.roots(), [0])
        self.assertEqual(graph.next(0), [1, 2])
        self.assertEqual(graph.next(1), [3, 4])
        self.assertEqual(graph.next(2), [5, 6])
        self.assertEqual(graph.next(3), [])
        self.assertEqual(graph.next(4), [])
        self.assertEqual(graph.next(5), [])
        self.assertEqual(graph.next(6), [0])

    def test_graph_with_two_roots(self):
        graph = generate_graph_with_two_roots()
        self.assertEqual(graph.roots(), [0, 2])
        self.assertEqual(graph.next(0), [1, 2])
        self.assertEqual(graph.next(1), [3, 4])
        self.assertEqual(graph.next(2), [5, 6])
        self.assertEqual(graph.next(3), [])
        self.assertEqual(graph.next(4), [])
        self.assertEqual(graph.next(5), [])
        self.assertEqual(graph.next(6), [])

    def test_bfs(self):
        graph = generate_graph()
        acc = []
        graph.bfs(acc, on_entry=lambda source, n, acc: acc.append(n))
        self.assertEqual(acc, [0, 1, 2, 3, 4, 5, 6])

    def test_bfs_with_loop(self):
        graph = generate_graph_with_loop()
        acc = []
        graph.bfs(acc, on_entry=lambda source, n, acc: acc.append(n))
        '''warning, the order of the nodes is not guaranteed, so we need to sort the list'''
        self.assertEqual(sorted(acc), sorted([0, 1, 2, 3, 4, 5, 6]))

    def test_bfs_with_two_roots(self):
        graph = generate_graph_with_two_roots()
        acc = []
        graph.bfs(acc, on_entry=lambda source, n, acc: acc.append(n))
        '''warning, the order of the nodes is not guaranteed, so we need to sort the list'''
        self.assertEqual(sorted(acc), sorted([0, 1, 2, 3, 4, 5, 6]))

    def test_predicate(self):
        graph = generate_graph()
        predicate = lambda n: n == 3
        print(graph.predicate_finder(predicate))

        self.assertEqual(graph.predicate_finder(predicate)[0], True)
        self.assertEqual(graph.predicate_finder(predicate)[1], [3])

    def test_predicate_greater_than(self):
        graph = generate_graph()
        predicate = lambda n: n > 3
        print(graph.predicate_finder(predicate))

        self.assertEqual(graph.predicate_finder(predicate)[0], True)
        #sort the list because the order is not guaranteed
        self.assertEqual(sorted(graph.predicate_finder(predicate)[1]), sorted([4, 5, 6]))

    def test_predicate_with_loop(self):
        graph = generate_graph_with_loop()
        predicate = lambda n: n == 3
        print(graph.predicate_finder(predicate))

        self.assertEqual(graph.predicate_finder(predicate)[0], True)
        self.assertEqual(graph.predicate_finder(predicate)[1], [3])

    def test_predicate_with_multiple_roots(self):
        graph = generate_graph_with_two_roots()
        predicate = lambda n: n == 3
        print(graph.predicate_finder(predicate))

        self.assertEqual(graph.predicate_finder(predicate)[0], True)
        self.assertEqual(graph.predicate_finder(predicate)[1], [3])

    def test_traces(self):
        graph = generate_graph()
        traces = graph.get_traces([3])
        print(traces)
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.simple_graph()  # Don't know why, but it runs all the test and no just the first one.


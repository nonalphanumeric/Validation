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
    dico = {0: [1, 2], 1: [3, 4], 2: [5, 6], 3: [], 4: [], 5: [], 6: [], 7: [2]}
    roots = [0, 7]
    return DicGraph(dico, roots)

def generate_complex_graph():
    #should have multiple roots, and cases of nodes with multiple parents
    dico = {0: [1, 2, 7, 8], 1: [3, 4], 2: [5, 6], 3: [], 4: [], 5: [], 6: [], 7: [5, 6], 8: [5, 6]}
    roots = [0, 1]
    return DicGraph(dico, roots)


class MyTestCase(unittest.TestCase):
    def test_simple_trace(self):
        graph = generate_graph()
        ptp = ParentTraceProxy.ParentTraceProxy(graph, graph.graph)
        self.assertEqual(ptp.get_trace(ptp.dict, 6), [6, 2, 0])
    def test_simple_traces(self):
        graph = generate_graph()
        ptp = ParentTraceProxy.ParentTraceProxy(graph, graph.graph)
        self.assertEqual(ptp.get_traces(ptp.dict, 6), [[6, 2, 0]])
    def test_trace_with_loop(self):
        graph = generate_graph_with_loop()
        ptp = ParentTraceProxy.ParentTraceProxy(graph, graph.graph)
        self.assertEqual(ptp.get_trace(ptp.dict, 6), [6, 2, 0])

    def test_trace_with_two_roots(self):
        graph = generate_graph_with_two_roots()
        ptp = ParentTraceProxy.ParentTraceProxy(graph, graph.graph)
        self.assertEqual(ptp.get_trace(ptp.dict, 6), [6, 2])

    def test_traces_with_two_roots(self):
        graph = generate_graph_with_two_roots()
        ptp = ParentTraceProxy.ParentTraceProxy(graph, graph.graph)
        self.assertEqual(ptp.get_traces(ptp.dict, 6), [[6, 2, 0], [6, 2, 7]])

    def test_complex_trace(self):
        graph = generate_complex_graph()
        ptp = ParentTraceProxy.ParentTraceProxy(graph, graph.graph)
        self.assertEqual(ptp.get_trace(ptp.dict, 6), [6, 2, 0])


if __name__ == '__main__':
    unittest.main()

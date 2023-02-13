from abc import abstractmethod

class TransitionRelation:
    """
    The TransitionRelation class defines the abstract methods that must be implemented by its subclasses.
    It represents a relationship between sources and destinations.
    """
    @abstractmethod
    def roots(self):
        """
        This abstract method returns the initial sources of the transition relation.
        """
        pass

    @abstractmethod
    def next(self, source):
        """
        This abstract method returns the destinations reachable from a given source.
        :param source: The source to get destinations from.
        :return: A list of destinations.
        """
        pass

    @abstractmethod
    def bfs(self, acc, on_entry=lambda source, n, acc: None,
            on_known=lambda source, n, acc: None,
            on_exit=lambda source, acc: None):
        """
        This abstract method performs a breadth-first search through the transition relation.
        :param acc: The accumulator used for the search.
        :param on_entry: A function to be called when entering a node.
        :param on_known: A function to be called when a node has already been visited.
        :param on_exit: A function to be called when exiting a node.
        :return: The final value of the accumulator.
        """
        pass

'''
This class makes a transition relation from a semantic graph.
/!\ Reminder: Semantic has configurations, and rules, those rules, when executed from a source, dictates the next configurations.

So, in a way, the transition relation is a graph which is explicit, the structure of the data is a dict.
With the semantic, we don't really have that structure but we can compute it using those rules. So, in a way, if one
'''

from Misc.transitionRelation import TransitionRelation


class SemanticToTransitionRelation(TransitionRelation):
    """
    This class creates a transition relation from a semantic graph.

    The SemanticToTransitionRelation class takes a semantic graph as input and creates a transition relation from it. The transition relation is a graph-like structure that explicitly shows the relationships between different configurations in the semantic graph.

    Attributes:
    semantic (SemanticTransitionRelation): The input semantic graph.

    Methods:
    roots()
        Returns the initial configurations of the semantic graph.
    next(source)
        Returns the configurations that can be reached from the given source configuration using the rules in the semantic graph.
    """

    def __init__(self, semantic):
        """
        The constructor for SemanticToTransitionRelation class.

        Parameters:
        semantic (SemanticTransitionRelation): The input semantic graph.
        """
        self.semantic = semantic

    def roots(self):
        """
        Returns the initial configurations of the semantic graph.

        Returns:
        list: The list of initial configurations in the semantic graph.
        """
        return self.semantic.initialConf()

    def next(self, source):
        """
        Returns the configurations that can be reached from the given source configuration using the rules in the semantic graph.

        Parameters:
        source (Any): The source configuration.

        Returns:
        list: The list of configurations that can be reached from the given source configuration.
        """
        enabled_rules = self.semantic.enabled_rules(source)
        new_configs = []
        # Here we determine the next elements by executing the rules on the source.
        for rule in enabled_rules:
            new_configs += self.semantic.execute(rule, source)
        return new_configs

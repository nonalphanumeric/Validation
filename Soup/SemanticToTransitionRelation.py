'''
This class makes a transition relation from a semantic graph.
/!\ Reminder: Semantic has configurations, and rules, those rules, when executed from a source, dictates the next configurations.

So, in a way, the transition relation is a graph which is explicit, the structure of the data is a dict.
With the semantic, we don't really have that structure but we can compute it using those rules. So, in a way, if one
'''
from abc import ABC

from Misc.transitionRelation import TransitionRelation


class SemanticToTransitionRelation(TransitionRelation):
    def __init__(self, semantic):
        self.semantic = semantic

    def roots(self):
        return self.semantic.initialConf()

    def next(self, source):
        enabled_rules = self.semantic.enabled_rules(source)
        new_configs = []
        #Here we determine the next elements by executing the rules on the source.
        for rule in enabled_rules:
            new_configs += self.semantic.execute(rule, source)
        return new_configs



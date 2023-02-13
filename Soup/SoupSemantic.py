import copy
from abc import ABC

from SemanticTransitionRelation import SemanticTransitionRelation


class SoupSemantic(SemanticTransitionRelation, ABC):
    '''
    SoupSemantic represents a class that inherits the properties and methods of the SemanticTransitionRelation and ABC classes.
    It represents a class that helps in representing a program as a transition relation.
    It contains the following methods:
        - __init__: initializes the class and takes one argument, 'program', which represents the program
        - initialConf: returns the initial configuration of the program as a list
        - enabledActions: returns a list of enabled actions based on the given source configuration
        - execute: takes a rule and a source configuration and executes the rule on the source to get the target configuration
    '''
    def __init__(self, program):
        '''
        Initializes the class and takes one argument, 'program', which represents the program
        '''
        self.program = program

    def initialConf(self):
        '''
        Returns the initial configuration of the program as a list
        '''
        return [self.program.ini]

    def enabledActions(self, source):
        '''
        Returns a list of enabled actions based on the given source configuration
        '''
        return list(filter(lambda r: r.guard(source), self.program.rules))

    def execute(self, rule, source):
        '''
        Takes a rule and a source configuration and executes the rule on the source to get the target configuration
        '''
        t = copy.deepcopy(source)
        rule.execute(t)  # t : un config cf class Rule
        return [t]






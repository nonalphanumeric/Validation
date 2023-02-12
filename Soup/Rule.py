import copy
from abc import ABC, abstractmethod


class Rule(ABC):
    @abstractmethod
    def __init__(self, name, guard):
        self.name = name
        self.guard = guard

    @abstractmethod
    def __str__(self):
        return self.name

    @abstractmethod
    def execute(self, config):
        # main things to change when implementing this abstraction
        pass


'''
Implementation of Rule so that it also has an action in the form of a lambda function
'''


class RuleAction(Rule, ABC):
    def __init__(self, name, guard, action):
        super().__init__(name, guard)
        self.action = action

    def execute(self, config):
        #copy the config
        print(config)
        res = copy.deepcopy(config)
        res = self.action(res)
        print(res)

        return [res]

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

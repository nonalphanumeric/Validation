import copy
from abc import ABC, abstractmethod


class Rule(ABC):
    """
    Abstract class that defines the structure of a rule in a semantic transition system.
    A rule consists of a name and a guard, which are both defined by the user.
    The execute method needs to be implemented by the user to define the specific actions that the rule should take.
    """
    @abstractmethod
    def __init__(self, name, guard):
        """
        Constructor for the Rule class.

        :param name: The name of the rule
        :type name: str
        :param guard: The guard condition for the rule. This is a lambda function that takes in a configuration and returns a boolean indicating whether the rule is enabled or not.
        :type guard: function
        """
        self.name = name
        self.guard = guard

    @abstractmethod
    def __str__(self):
        """
        The string representation of the rule, which is its name.

        :return: The name of the rule
        :rtype: str
        """
        return self.name

    @abstractmethod
    def execute(self, config):
        """
        The method that defines what the rule should do when executed.
        This method should be implemented by the user.

        :param config: The configuration that the rule is executed on
        :type config: object
        :return: The new configuration after the rule has been executed
        :rtype: object
        """
        pass


class RuleAction(Rule, ABC):
    """
    Implementation of the Rule class, where the rule also has an action in the form of a lambda function.
    """
    def __init__(self, name, guard, action):
        """
        Constructor for the RuleAction class.

        :param name: The name of the rule
        :type name: str
        :param guard: The guard condition for the rule. This is a lambda function that takes in a configuration and returns a boolean indicating whether the rule is enabled or not.
        :type guard: function
        :param action: The action that the rule should take when executed. This is a lambda function that takes in a configuration and returns the new configuration after the rule has been executed.
        :type action: function
        """
        super().__init__(name, guard)
        self.action = action

    def execute(self, config):
        """
        The method that defines what the rule should do when executed.
        This method creates a deep copy of the configuration and then executes the action on the copied configuration.

        :param config: The configuration that the rule is executed on
        :type config: object
        :return: The new configuration after the rule has been executed
        :rtype: object
        """
        #copy the config
        res = copy.deepcopy(config)
        res = self.action(res)

        return [res]

    def __str__(self):
        """
        The string representation of the rule, which is its name.

        :return: The name of the rule
        :rtype: str
        """
        return self.name

    def __repr__(self):
        """
        The string representation of the rule, which is its name.

        :return: The name of the rule
        :rtype: str
        """
        return self.name

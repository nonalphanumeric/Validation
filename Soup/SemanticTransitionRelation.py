class SemanticTransitionRelation(ABC):
    '''
    Abstract base class for defining a semantic transition relation.
    A semantic transition relation is a relation between configurations and the actions that can be executed
    in these configurations.
    '''

    @abstractmethod
    def initialConf(self):
        '''
        Returns the initial configuration(s) of the program.
        '''
        pass

    @abstractmethod
    def enabledActions(self, source):
        '''
        Returns a list of the enabled actions in the given configuration.
        :param source: the given configuration
        '''
        pass

    @abstractmethod
    def execute(self, a, source):
        '''
        Executes the given action in the given configuration and returns the resulting configuration(s).
        :param a: the given action
        :param source: the given configuration
        '''
        pass

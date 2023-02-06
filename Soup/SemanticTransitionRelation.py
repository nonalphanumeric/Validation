from abc import abstractmethod, ABC


class SemanticTransitionRelation(ABC):

    @abstractmethod
    def initialConf(self):
        pass

    @abstractmethod
    def enabledActions(self,source):
        pass

    @abstractmethod
    def execute(self,a,source):
        pass

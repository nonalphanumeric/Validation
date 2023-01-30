from abc import abstractmethod, ABC


class InputSemanticTransitionRelation(ABC):

    @abstractmethod
    def initial(self):
        pass

    @abstractmethod
    def actions(self,input,source):
        pass

    @abstractmethod
    def execute(self,action, input, source):
        pass

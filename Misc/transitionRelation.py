from abc import abstractmethod


class TransitionRelation:
    @abstractmethod
    def roots(self):
        pass

    @abstractmethod
    def next(self, source):
        pass

    @abstractmethod
    def bfs(self, acc, on_entry=lambda source, n, acc: None,
            on_known=lambda source, n, acc: None,
            on_exit=lambda source, acc: None):
        pass
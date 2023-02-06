class DicGraph:
    def __init__(self, dico, roots):
        self.graph = dico  # dico a utiliser
        self.entrypoints = roots  # les points d'entree

    def roots(self):
        return self.entrypoints

    def next(self, source):
        try:
            return self.graph[source]
        except KeyError:
            return []

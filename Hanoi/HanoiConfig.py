class HanoiConfig:
    def __init__(self, n, k):
        self.n = n
        self.k = k

    def __eq__(self, other):
        return self.n == other.n and self.k == other.k

    def __hash__(self):
        """print("The hash is : ")
        return hash((self.n, self.k))"""
        return 1
    def __str__(self):
        return "hanoi configurtation %d" % self.n, self.k

    def __repr__(self):
        return self.__str__()
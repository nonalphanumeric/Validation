class IdentityProxy:
    def __init__(self,operand):
        self.operand = operand

    def __getattr__(self, attr):
        return getattr(self.operand,attr)
    
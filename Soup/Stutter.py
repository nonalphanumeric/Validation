from Soup.Rule import Rule

'''
St-st-stutter.
Its in the name. We just return the same configuration.
'''
class Stutter(Rule):
    def __init__(self):
        super().__init__(None, None)

    def execute(self, config):
        return [config]

class SoupProgram:
    '''
    Class that represents a soup program.
    It contains the initial configuration `ini` and the list of `rules`
    '''

    def __init__(self, ini):
        '''
        Initializes a SoupProgram instance with the initial configuration `ini`.
        '''
        self.ini = ini
        self.rules = []

    def add(self, rule):
        '''
        Adds a `rule` to the list of rules in the soup program.
        '''
        self.rules.append(rule)

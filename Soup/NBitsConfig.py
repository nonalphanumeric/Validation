from SoupProgram import SoupProgram

class NBitsConfig:
    def __init__(self, n): #n nb de bits
        self.value = 0
    def __eq__(self):
        #blabla
    def __hash__(self):
        #blabla


soup = SoupProgram(NBitsConfig())

def flip0():
    pass

def flip1():
    pass

#verification de predicat
soup.add('flip0', lambda c : True, flip0())
soup.add('flip1', lambda c:True, flip1())


        
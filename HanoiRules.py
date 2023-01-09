from transitionRelation import TransitionRelation
from HanoiConfig import HanoiConfig
class HanoiRules(TransitionRelation):

        def __init__(self,n,k):
            self.n = n;
            self.hanoiConfig = HanoiConfig(n,k)
            self.initial = [[1,2,3],[],[]]

        def next(self, source):
            all_config = []
            for i in source:
                for j in source:
                    #si la selection (i,j) correspond à deux tours distinctes:
                    if len(i) != 0:
                        if len(j) == 0 or i[0] < j[0]:


        def
        """def roots(self):"""


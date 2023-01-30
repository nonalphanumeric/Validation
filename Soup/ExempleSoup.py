from Rule import Rule
from SoupProgram import SoupProgram
from SoupSemantic import SoupSemantic
from Misc.Traversal import predicate_finder
from Str2Tr import Str2Tr

iC = [False, False]
# iC[0] = False : alice pas dans le jardin
# iC[1] = False : bob n'est pas dans le jardin
rule1 = Rule("alice veut jardin", lambda c: not c[0] and not c[1], None)
rule2 = Rule("bob veut jardin" , lambda c: not c[0] and not c[1], None)
rule3 = Rule("alice veut rentrer", lambda c: True, None)
rule4 = Rule("bob veut rentrer", lambda c: True, None)


p = SoupProgram(iC)
s = SoupSemantic(p)
tr = Str2Tr(s)
predicate_finder(tr, lambda c: c.x == c.y)


from transitionRelation import TransitionRelation
from SoupSemantic import SoupSemantic
from SoupProgram import SoupProgram
class Str2Tr(TransitionRelation):
    """
    comments
    """

    program = SoupProgram(iC)
    s = SoupSemantic(program)
    roots = s.initialConfigurations()
    next(s)



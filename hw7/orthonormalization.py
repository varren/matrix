from orthogonalization import orthogonalize, aug_orthogonalize
from math import sqrt
from mat import transpose
from matutil import coldict2mat, mat2coldict 


def normalize(v): return v/sqrt(v*v)

def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''

    return [normalize(v) for v in orthogonalize(L)]


def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    V, S = aug_orthogonalize(L)
    Q = orthonormalize(L)
    R = mat2coldict(transpose(coldict2mat(V)) * coldict2mat(Q) * coldict2mat(S))
    
    return (Q,[x for x in R.values()])

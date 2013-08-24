# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from independence import is_independent


## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    while True:
        u = list2vec([randGF2() for x in range(6)])
        if a0*u == s and b0*u == t:
            return u
    



## Problem 2
# Give each vector as a Vec instance
from itertools import combinations

def allInd(vecs):
    return all(is_independent(list(sum(x,()))) for x in combinations(vecs,3))

def selectRandom():
    vecs =[(a0,b0)]
    for x in range(4):
        a = list2vec([randGF2() for x in range(6)])
        b = list2vec([randGF2() for x in range(6)])
        vecs.append((a,b))
    return vecs

while True:
    vecs = selectRandom()
    if allInd(vecs):
        break

#print (vecs)
"""
while len(vecs) < 5:
    solution = vecs[:]
    a1 = list2vec([randGF2() for x in range(6)])
    b1 = list2vec([randGF2() for x in range(6)])
    if is_independent([a1,b1]):
        solution += [(a1,b1)]
    if allInd(vecs):
        vecs = solution[:]
print (vecs)
"""
secret_a0 = a0
secret_b0 = b0
secret_a1 = vecs[1][0]
secret_b1 = vecs[1][1]
secret_a2 = vecs[2][0]
secret_b2 = vecs[2][1]
secret_a3 = vecs[3][0]
secret_b3 = vecs[3][1]
secret_a4 = vecs[4][0]
secret_b4 = vecs[4][1]


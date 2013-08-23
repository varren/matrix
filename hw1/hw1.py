# Please fill out this stencil and submit using the provided submission script.

from GF2 import one
import itertools


## Problem 1
p1_u = [ 0, 4]
p1_v = [-1, 3]
p1_v_plus_u = [p1_v[x] + p1_u[x] for x in range(len(p1_u))]
p1_v_minus_u = [p1_v[x] - p1_u[x] for x in range(len(p1_u))]
p1_three_v_minus_two_u = [3 * p1_v[x] - 2 * p1_u[x] for x in range(len(p1_u))]



## Problem 2
p2_u = [-1,  1, 1]
p2_v = [ 2, -1, 5]
p2_v_plus_u = [p2_v[x] + p2_u[x] for x in range(len(p2_u))]
p2_v_minus_u = [p2_v[x] - p2_u[x] for x in range(len(p2_u))]
p2_two_v_minus_u = [2 * p2_v[x] - p2_u[x] for x in range(len(p2_u))]
p2_v_plus_two_u = [p2_v[x] + 2 * p2_u[x] for x in range(len(p2_u))]


## Problem 3
# Write your answer using GF2's one instead of the number 1
v = [0,one,one]
u = [one,one,one]
p3_vector_sum_1 = [v[x] + u[x] for x in range(len(u))]
p3_vector_sum_2 = [v[x] + u[x] + u[x] for x in range(len(u))]



## Problem 4
# Please express your solution as a set of the letters corresponding to the solutions.
# For example, {'a','b','c'} is the subset consisting of:
#   a (1100000), b (0110000), and c (0011000).
# Leave an empty set if it cannot be expressed in terms of the other vectors.

u_0010010 = {'e', 'd', 'c'}
u_0100010 = {'e', 'd', 'c','b'}



## Problem 5
# Use the same format as the previous problem

v_0010010 = {'d','c'}
v_0100010 = set()



## Problem 6

u = [1, 0]
v = [5, 4321]
uv_a = sum([u[x] * v[x] for x in range(len(u))])

u = [0, 1]
v = [12345, 6]
uv_b = sum([u[x] * v[x] for x in range(len(u))])

u =[-1, 3]
v = [5, 7]
uv_c = sum([u[x] * v[x] for x in range(len(u))])

uv_d = sum([-1/2, -1/2])



## Problem 7
# use 'one' instead of '1'
def mul(u,v):
    return sum([u[x] * v[x] for x in range(len(u))])
    
a = [one, one, one, one]
b = [one, 0, one, 0] 
c = [one, one, 0, 0] 

possibleValues = [x for x in itertools.product([one,0], repeat=4)]

def found(x):
    return mul(x,a) == mul(x, b) and mul(x,a) == mul(x, c) and mul(x,a) == one

x_gf2full = [list(x) for x in possibleValues if found(x)]
x_gf2 = x_gf2full[0]


## Problem 8
v1 = [2,3,-4, 1]
v2 = [1,-5,2,0]
v3 = [4,1,-1,-1]


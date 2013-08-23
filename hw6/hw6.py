# version code 988
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
import echelon
from GF2 import one



## Problem 1
# Write each matrix as a list of row lists

echelon_form_1 = [[1,2,0,2,0],
                  [0,1,0,3,4],
                  [0,0,2,3,4],
                  [0,0,0,2,0],
                  [0,0,0,0,4]]

echelon_form_2 = [[0,4,3,4,4],
                  [0,0,4,2,0],
                  [0,0,0,0,1],
                  [0,0,0,0,0]]

echelon_form_3 = [[1,0,0,1],
                  [0,0,0,1],
                  [0,0,0,0]]

echelon_form_4 = [[1,0,0,0],
                  [0,1,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]
## Problem 2
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
    '''
    
    Y = 0

    for x in range(len(A)):
        for y in range(len(A[0])):

            if y < Y and A[x][y]:
                return False
    
            if y >= Y:
                Y += 1
                
                if A[x][y]:
                    break

    return True




## Problem 3
# Give each answer as a list

echelon_form_vec_a = [1,0,3,0]
echelon_form_vec_b = [-3,0,-2,3]
echelon_form_vec_c = [-6,1,2,0,2]



## Problem 4
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None".

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [-3,-10,-4,1,0]



## Problem 5
def echelon_solve(rowlist, label_list, b):
    '''
    Input:
        - rowlist: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in rowlist
        - b: a vector (represented as a list)
    Output:
        - Vec x such that rowlist * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})] 
    >>> b_list = [one,0,one]>>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list)
    Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    '''
    from vecutil import zero_vec
    D = rowlist[0].D
    x = zero_vec(D)
    for j in reversed(range(len(rowlist))):
        row = rowlist[j]
        l = label_list[j]
        for i in list(D):
            l = i
            if(row[l] != 0):break
        if row[l] != 0:
            x[l] = (b[j] - x*row)/row[l]

    return x

"""
def solve(A, b):
    M = echelon.transformation(A)
    U = M*A
    col_label_list = sorted(A.D[1])
    U_rows_dict = mat2rowdict(U)
    rowlist = [U_rows_dict[i] for i in U_rows_dict]
    return echelon_solve(rowlist,col_label_list, M*b)
"""
## Problem 6
D = {"A", "B", "C", "D" }
d = {"a", "b", "c", "d" }
M = rowdict2mat({"a": Vec(D, {"A": one, "B": one, "C": 0,   "D": one}),
                 "b": Vec(D, {"A": one, "B": 0,   "C": 0,   "D": one}),
                 "c": Vec(D, {"A": one, "B": one, "C": one, "D": one}),
                 "d": Vec(D, {"A": 0,   "B": 0,   "C": one, "D": one})})

g = Vec(d,{"a":one,"b": 0,"c": one,"d": 0})

rowlist =   list(mat2rowdict(M))  # Provide as a list of Vec instances
label_list = ["A", "B", "C", "D" ] # Provide as a list
b = []#solve(M, g)              # Provide as a list



## Problem 7
null_space_rows_a = {...} # Put the row numbers of M from the PDF



## Problem 8
null_space_rows_b = {...}



## Problem 9
# Write each vector as a list
closest_vector_1 = [...]
closest_vector_2 = [...]
closest_vector_3 = [...]



## Problem 10
# Write each vector as a list

project_onto_1 = [...]
projection_orthogonal_1 = [...]

project_onto_2 = [...]
projection_orthogonal_2 = [...]

project_onto_3 = [...]
projection_orthogonal_3 = [...]



## Problem 11
norm1 = ...
norm2 = ...
norm3 = ...


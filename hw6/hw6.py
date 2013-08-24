# version code 988
# Please fill out this stencil and submit using the provided submission script.
from vecutil import list2vec
from matutil import *
import echelon
from GF2 import one
from vecutil import zero_vec



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
    >>> b_list = [one,0,one]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list)
    Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    '''
    D = rowlist[0].D
    x = zero_vec(D)
    for j in reversed(range(len(rowlist))):
        row = rowlist[j]
        l = 0
        for i in label_list:
            l = i
            if(row[l] != 0):break
        if row[l] != 0:
            x[l] = (b[j] - x*row)/row[l]

    return x



def solve(A, b):
    M = echelon.transformation(A)
    U = M*A
    col_label_list = sorted(A.D[1])
    U_rows_dict = mat2rowdict(U)
    rowlist = [U_rows_dict[i] for i in U_rows_dict]
    return echelon_solve(rowlist,col_label_list, M*b)



## Problem 6

D = {"A", "B", "C", "D" }
d = {"a", "b", "c", "d" }
n = {0,1,2,3}

A = Mat((d, D), {("a","A"): one, ("a","B"): one, ("a","C"): 0,   ("a","D"): one,
                 ("b","A"): one, ("b","B"): 0,   ("b","C"): 0,   ("b","D"): one,
                 ("c","A"): one, ("c","B"): one, ("c","C"): one, ("c","D"): one,
                 ("d","A"): 0,   ("d","B"): 0,   ("d","C"): one, ("d","D"): one})

M = Mat((n, d), {(0,"a"): one, (0,"b"): 0,   (0,"c"): 0,   (0,"d"): 0,
                 (1,"a"): one, (1,"b"): one,   (1,"c"): 0,   (1,"d"): 0,
                 (2,"a"): one, (2,"b"): 0, (2,"c"): one, (2,"d"): 0,
                 (3,"a"): one, (3,"b"): 0,   (3,"c"): one, (3,"d"): one})

g = Vec(d,{"a":one,"b": 0,"c": one,"d": 0})

U = M*A
col_label_list = sorted(A.D[1])
U_rows_dict = mat2rowdict(U)
bVec = M*g

rowlist = [U_rows_dict[i] for i in U_rows_dict]
label_list = col_label_list
b =  [bVec[x] for x in sorted(bVec.D)]

## Problem 7
null_space_rows_a = {3,4} # Put the row numbers of M from the PDF



## Problem 8
null_space_rows_b = {4}



## Problem 9
# Write each vector as a list
def closest(a, b):
    a = list2vec(a)
    b = list2vec(b)
    sigma = ((b*a)/(a*a))*a if a*a !=0 else 0
    return [sigma[x] for x in sorted(sigma.D)]

a = [1,2] 
b = [2,3]
closest_vector_1 = closest(a,b)
a = [0, 1, 0]
b = [1.414, 1, 1.732] 
closest_vector_2 = closest(a,b)
a = [-3,-2,-1,4]
b = [7,2,5,0]
closest_vector_3 = closest(a,b)



## Problem 10
# Write each vector as a list
def orthogonal(a,b):    
    a = list2vec(a)
    b = list2vec(b)
    sigma = b - ((b*a)/(a*a))*a if a*a !=0 else 0
    return [sigma[x] for x in sorted(sigma.D)]
 

a = [3, 0]
b = [2, 1]
project_onto_1 = closest(a,b)
projection_orthogonal_1 = orthogonal(a,b)

a = [1, 2,-1]
b = [1, 1, 4]
project_onto_2 = closest(a,b)
projection_orthogonal_2 = orthogonal(a,b)

a = [3,3,12]
b = [1,1,4]
project_onto_3 = closest(a,b)
projection_orthogonal_3 = orthogonal(a,b)



## Problem 11
norm1 = 3
norm2 = 4
norm3 = 1


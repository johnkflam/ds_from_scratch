
#<<export>>
from typing import List, Tuple, Callable
import math

Vector = List[float]
Matrix = List[List[float]] # inner list represents a row of the matrix





def vector_add(v1: Vector, v2: Vector) -> Vector:
    """Adding vectors"""
    assert len(v1)==len(v2),"vectors must be the same length"
    
    return [x+y for x,y in zip(v1,v2)]

assert vector_add([1,2],[2,1])==[3,3]

def vector_subtract(v1: Vector, v2: Vector) -> Vector:
    """Substract vectors"""
    assert len(v1)==len(v2),"vectors must be the same length"
    
    return [x - y for x,y in zip(v1,v2)]

assert vector_subtract([3,4],[1,2])==[2,2]

def check_vectors_size(v_list:Vector) -> bool:
    """check if the length of all vectors are the same"""
    assert v_list,'v_list is required'
    
    size=len(v_list[0])
    return all(len(n)==size for n in v_list)

assert check_vectors_size([[1,2,3],[1,2,4],[3,3,3]]), "vectors have different length"


def vector_sum(vectors: List[Vector]) -> Vector:
    """ add vectors in list"""
    assert vectors,'vectors is required'
    
    assert check_vectors_size(vectors),'all vector size must be the same'
    
    size=len(vectors[0])
    return [sum(v[n] for v in vectors)# sum all the elements with the same index (inner loop)
        for n in range(size)] # loop through each index (outer loop)

assert vector_sum([[1,2,3],[1,2,4],[3,3,3]])==[5,7,10]

def scalar_multiply(c: float, v: Vector) -> Vector:
    """ multiply every element by c"""
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1,2,3])==[2,4,6]

def vector_mean(vectors: List[Vector]) -> float:
    """ computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n,vector_sum(vectors))

assert vector_mean([[1,2],[3,4]])==[2,3]

 def dot(v: Vector, w: Vector) -> float:
    """ sum of their componentwise products """
    assert len(v)==len(w)
    
    return sum(v_i * w_i  for v_i, w_i in zip(v,w))

assert dot([2,2],[3,3])==12.0

def sum_of_squares(v: Vector) -> float:
    """ Return v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

assert sum_of_squares([2,3])==2*2+3*3==13

def magnitude(v: Vector) -> float:
    """ Returns the magnitude (or length) of v"""
    return math.sqrt(sum_of_squares(v))

assert magnitude([3,4]) == 5

def distance(v: Vector, w: Vector) -> float:
    """ returns distance between 2 vectors """
    return magnitude(vector_subtract(v, w))

print(distance([3,4],[2,3]))
print(math.sqrt((3-2)^2 + (4-3)^2))


def shape(A: Matrix) -> Tuple[int,int]:
    """Returns (# of rows of A, # of columns of A)"""
    rows = len(A)
    cols = len(A[0]) if A[0] else 0
    return (rows,cols)

A = [[2,3],[3,5],[6,7]]
assert shape(A)==(3,2)


def get_row(A: Matrix, i: int) -> Vector:
    """Returns the i-th row of A (as a Vector)"""
    return A[i]

def get_column(A: Matrix, j: int) -> Vector:
    """Returns the j-th column of A (as a Vector)"""
    return [A_i[j] # get the element from j
               for A_i in A] #for each row in A


def make_matrix(num_rows: int,
               num_cols: int,
               entry_fn: Callable[[int, int], float]) -> Matrix:
    """
        Returns a num_rows x num_cols matrix
        whose (i,j)-th entry is entry_fn(i,j)
    """
    return [
        [
            entry_fn(i,j)
                for j in range(num_cols) 
        ]
        for i in range(num_rows)
    ]

def identity_matrix(n: int) -> Matrix:
    """Returns the n x n identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)





def get_friends(friends_matrix,row):
    return [i
            for i,is_friend in enumerate(friends_matrix[row])
               if is_friend]




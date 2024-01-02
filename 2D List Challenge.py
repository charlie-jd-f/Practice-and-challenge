# 2-D List Challenge
#
# Create a function which takes in a matrix as an input and returns
# its transpose
#
# e.g.
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# 
# becomes
#
# [1, 4, 7]
# [2, 5, 6]
# [3, 6, 9]


# Pseudo code
# find dimension of the matrix
# create a new matrix which has the dimensions of the transppose
# e.g. 2 x 3 matrix -> new matrix is 3 x 2
# loop through each element
# if index x = index y, then stay the same
# if index x != index y, make it equal new_matrix[y][x]
# print/return the new matrix

def transpose(matrix):

    dim_row = len(matrix)
    dim_col = len(matrix[0])

    new_matrix = [[" " for _ in range(dim_row)] for _ in range(dim_col)]

    for y in range(dim_row):
        for x in range(dim_col):
            new_matrix[x][y] = matrix[y][x]

    return new_matrix

def display_matrix(matrix):
    for line in matrix:
        print(line)
    return

matrix1 = [[1,2,3],
          [4,5,6],
          [7,8,9]]

matrix2 = [[1,2,3],
           [4,5,6]]

matrix3 = [[1],
           [2],
           [3]]

matrix4 = [[1,1],
           [1,1],
           [1,1]]

display_matrix(transpose(matrix4))

import numpy as np

# This is the code for a function to obtain the matrix of minors of any m * m square matrix represented by a 2D Numpy array

# The code uses Numpy's inbuilt np.linalg.det() function for finding determinants

# defining the inner function to obtain M_{i, j}:

def get_minor_element(input_matrix, input_row_index, input_col_index):

    input_matrix_edited = input_matrix

    input_matrix_edited = np.delete(input_matrix_edited, obj = input_row_index, axis = 0)
    input_matrix_edited = np.delete(input_matrix_edited, obj = input_col_index, axis = 1)

    return np.linalg.det(input_matrix_edited)


# the function to obtain the matrix of minors M

def get_matrix_of_minors(input_matrix):

    if type(input_matrix) != np.ndarray or input_matrix.ndim != 2:
        return 'Please input a square matrix in the form of a numpy array'

    # Checking whether the matrix is square - len(row) = the number of columns, while len(input_matrix) = the number of rows

    if all(len(row) == len(input_matrix) for row in input_matrix) == False:
        return 'Please input a square matrix'

    output_matrix = np.zeros(shape = input_matrix.shape)

    for i in range(0, len(input_matrix)):
        for j in range(0, len(input_matrix[0])):

            output_matrix[i, j] = get_minor_element(input_matrix, i, j)

    return output_matrix

test_matrix = np.array([[4, 5, 6], [1, 2, 1], [8, 1, 4]])

test_matrix_not_square = np.array([[4, 5, 6], [1, 2, 1], [8, 1, 4],[8, 1, 4]])

test_list = [[1, 3], [2, 7]]

# Testing with a legitimate input:

print(get_matrix_of_minors(test_matrix))

# And with some illegitimate inputs:

print(get_matrix_of_minors(test_matrix_not_square))
print(get_matrix_of_minors(test_list))
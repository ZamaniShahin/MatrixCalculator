

def take_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    if(rows >10 or cols >10):
        return None
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
    
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result
def subtract_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    
    return result

    def multiply_matrices(matrix1, matrix2):
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix2[0])):
                element = 0
                for k in range(len(matrix2)):
                    element += matrix1[i][k] * matrix2[k][j]
                row.append(element)
            result.append(row)
    
    return result

    def determine_matrix(matrix):
        if len(matrix) != len(matrix[0]):
            return None
        
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
        det = 0
        for i in range(len(matrix)):
            sign = (-1) ** i
            sub_matrix = [row[:i] + row[i+1:] for row in matrix[1:]]
            sub_det = determine_matrix(sub_matrix)
            det += sign * matrix[0][i] * sub_det
    
    return det
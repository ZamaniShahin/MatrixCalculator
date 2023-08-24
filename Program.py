# Define os lib and initial clear for clearing console.
import os
clear = lambda: os.system('cls')

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

def swap_matrices(matrix1, matrix2):
    return matrix2, matrix1
def add_matrix_into_another(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

# Take two matrices from the user
clear()
print("Enter the first matrix:" , end='\n')
matrix1 = take_matrix()
if(matrix1 == None):
    print('Your Given Matrix Is Not Compatible With 10*10 Maximum Matrix Length.')
    quit()
print("Enter the second matrix:")
matrix2 = take_matrix()
if(matrix2 == None):
    print('Your Given Matrix Is Not Compatible With 10*10 Maximum Matrix Length.')
    quit()

#----------------------------------------------------------------------------------

while(True):
    print('*****************************************',end='\n')
    flag = int(input('Enter Your Option : \n0.End Operation\n1.Addition.\n2.Substraction.\n3.Multiplicarion.\n4.Determination.\n5.Swap Matrices.\n6.Add A Matrix Into Other one.\n'))
    clear()
    if(flag ==0):
        break
    elif(flag == 1):
        # Addition Tasks
        if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
            addition = add_matrices(matrix1, matrix2)
            print("\nAddition of the matrices:")
            print_matrix(addition)
    elif(flag == 2):
        #Substraction Tasks
        if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
            subtraction = subtract_matrices(matrix1, matrix2)
            print("\nSubtraction of the matrices:")
            print_matrix(subtraction)
    elif(flag ==3):
        #Multiplication Tasks
        if len(matrix1[0]) == len(matrix2):
            multiplication = multiply_matrices(matrix1, matrix2)
            print("\nMultiplication of the matrices:")
            print_matrix(multiplication)
    elif(flag == 4):
        #Determine Tasks
        if len(matrix1) == len(matrix1[0]):
            det1 = determine_matrix(matrix1)
            det2 = determine_matrix(matrix2)
            print("\nDeterminant of the first matrix:", det1)
            print("Determinant of the second matrix:", det2)
    elif(flag == 5):
        #Swap Tasks
        swapped_matrix1, swapped_matrix2 = swap_matrices(matrix1, matrix2)
        print("\nSwapped matrices:")
        print("Matrix 1:")
        print_matrix(swapped_matrix1)
        print("\nMatrix 2:")
        print_matrix(swapped_matrix2)
    elif(flag == 6):
        # Add Matrix To Other One Tasks
        if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
            addition = add_matrix_into_another(matrix1, matrix2)
            print("\nAdding one matrix into the other:")
            print_matrix(addition)
    else:
        print('Please Enter An Option Between 1 to 6 .')
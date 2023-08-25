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

def divide_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            try:
                value = matrix1[i][j] / matrix2[i][j]
            except ZeroDivisionError:
                value = 0
            row.append(value)
        result.append(row)
    return result
def mult_by_a_number(a , matrix1):
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            matrix1[i][j] *= a
    return matrix1

clear()

matrix1 = None
matrix2 = None
#----------------------------------------------------------------------------------

while(True):
    print('*****************************************',end='\n')
    flag = int(input('Enter Your Option : \n0.End Operation.\n1.Enter the first matrix:\n2.Enter the second matrix:'+
    '\n3.Transfer Matrix1 Into Matrix2.\n4.Transfer Matrix2 Into Matrix1.\n5.Matrix1 = Matrix1 * Matrix2.'+
    '\n6.Matrix1 = Matrix1 + Matrix2.\n7.Matrix1 = Matrix1 / Matrix2\n8.Matrix1 = Matrix1 - Matrix2\n9.Matrix1 = a * Matrix1'+
    '\n10.Determination For Matrix1.'+
    '\n11.DeterMination For Matrix2\n12.Display Matrix1\n13.Display Matrix2.\n'))
    clear()
    if(flag ==0):
        break
    elif(flag == 1):
        # Take two matrices from the user
        print("Enter The Matrix" , end='\n')
        matrix1 = take_matrix()
        if(matrix1 == None):
            print('Your Given Matrix Is Not Compatible With 10*10 Maximum Matrix Length.')
    elif(flag == 2):
        # Take two matrices from the user
        print("Enter The Matrix")
        matrix2 = take_matrix()
        if(matrix2 == None):
            print('Your Given Matrix Is Not Compatible With 10*10 Maximum Matrix Length.')
    elif(flag == 3):
        if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
            matrix1 = matrix2
    elif(flag == 4):
        if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
            matrix2 = matrix1
    elif(flag == 5):
        #Multiplication Tasks
        if len(matrix1[0]) == len(matrix2):
            matrix1 = multiply_matrices(matrix1, matrix2)
            print("\nMultiplication of the matrices:")
            print_matrix(matrix1)
        else:
            print('Matrix Sizes Are Not Compatible')
    elif(flag == 6):
        # Addition Tasks
        if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
            matrix1 = add_matrices(matrix1, matrix2)
            print("\nAddition of the matrices:")
            print_matrix(matrix1)
        else:
            print('Matrices Sizes Are Not Compatible For This Operation!')
    elif(flag == 7):
        #Divide Tasks
        if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
            matrix1 = divide_matrices(matrix1, matrix2)
            print_matrix(matrix1)
        else:
            print('Matrices Sizes Are Not Compatible For This Operation!')
    elif(flag == 8):
        #Substraction Tasks
        if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
            matrix1 = subtract_matrices(matrix1, matrix2)
            print("\nSubtraction of the matrices:")
            print_matrix(matrix1)
        else:
            print('Matrices Sizes Are Not Compatible For This Operation!')
    elif(flag == 9):
        a = float(input('Please Enter a: '))
        matrix1 = mult_by_a_number(a,matrix1)
        print_matrix(matrix1)
    elif(flag == 10):
        #Determine Tasks
        if len(matrix1) == len(matrix1[0]):
            det1 = determine_matrix(matrix1)
            print("Determinant of the first matrix:", det1)
        else:
            print('This Is Not An Squared Matrix.')
    elif(flag == 11):
        #Determine Tasks
        if len(matrix2) == len(matrix2[0]):
            det2 = determine_matrix(matrix2)
            print("Determinant of the second matrix:", det2)
        else:
            print('This Is Not An Squared Matrix.')
    elif(flag ==12):
        if(matrix1 != None):
            print_matrix(matrix1)
        else:
            print('Your Matrix Is Empty!\nPlease Enter It First')
    elif(flag ==13):
        if(matrix2 != None):
            print_matrix(matrix2)
        else:
            print('Your Matrix Is Empty!\nPlease Enter It First')
    else:
        print('Please Enter An Option Between 1 to 6 .')
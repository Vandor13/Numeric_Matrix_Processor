def get_matrix_from_input(name):
    matrix = []
    n, m = [int(x) for x in input("Enter size of {} matrix: > ".format(name)).split()]
    print("Enter {} matrix:".format(name))
    for _ in range(n):
        matrix.append([float(x) for x in input("> ").split()])
    return matrix


def add_matrices(matrix1, matrix2):
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        new_matrix = []
        for i in range(len(matrix1)):
            row1 = matrix1[i]
            row2 = matrix2[i]
            new_row = []
            for j in range(len(matrix1[0])):
                new_row.append(row1[j] + row2[j])
            new_matrix.append(new_row)
        return new_matrix
    else:
        return None


def multiply_matrix_with_scalar(matrix, scalar):
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element * scalar)
        new_matrix.append(new_row)
    return new_matrix


def multiply_matrices(matrix1, matrix2):
    if len(matrix2) != len(matrix1[0]):
        return None
    new_matrix = []
    for row in matrix1:
        new_row = []
        for i in range(len(matrix2[0])):
            new_element = 0
            for j in range(len(row)):
                new_element += row[j] * matrix2[j][i]
            new_row.append(new_element)
        new_matrix.append(new_row)
    return new_matrix


def transpose_matrix_main_diagonal(matrix):
    new_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


def transpose_matrix_side_diagonal(matrix):
    new_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[-j-1][-i-1] = matrix[i][j]
    return new_matrix


def transpose_matrix_vertical_line(matrix):
    new_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[i][-j-1] = matrix[i][j]
    return new_matrix


def transpose_matrix_horizontal_line(matrix):
    new_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[-i-1][j] = matrix[i][j]
    return new_matrix


def print_matrix(matrix):
    for i in range(len(matrix)):
        print(str(matrix[i])[1:-1].replace(",", ""))


def transpose_menu():
    while True:
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")
        user_choice = int(input("Your choice: > "))
        if 1 <= user_choice <= 4:
            break
        else:
            print("Input not recognized. Please try again")
            print()
    matrix_a = get_matrix_from_input("the")
    if user_choice == 1:
        result_matrix = transpose_matrix_main_diagonal(matrix_a)
    elif user_choice == 2:
        result_matrix = transpose_matrix_side_diagonal(matrix_a)
    elif user_choice == 3:
        result_matrix = transpose_matrix_vertical_line(matrix_a)
    elif user_choice == 4:
        result_matrix = transpose_matrix_horizontal_line(matrix_a)
    print("The result is:")
    print_matrix(result_matrix)
    print()


def main_menu():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("0. Exit")
        user_choice = int(input("Your choice: > "))
        if 0 <= user_choice <= 4:
            break
        else:
            print("Input not recognized. Please try again")
            print()
    if user_choice == 0:
        return False
    elif user_choice == 1:
        matrix_a = get_matrix_from_input("first")
        matrix_b = get_matrix_from_input("second")
        result_matrix = add_matrices(matrix_a, matrix_b)
        if result_matrix is None:
            print("The operation cannot be performed.")
            print()
        else:
            print("The result is:")
            print_matrix(result_matrix)
            print()
    elif user_choice == 2:
        matrix_a = get_matrix_from_input("the")
        multi = int(input("Enter constant: > "))
        result_matrix = multiply_matrix_with_scalar(matrix_a, multi)
        print("The result is:")
        print_matrix(result_matrix)
        print()
    elif user_choice == 3:
        matrix_a = get_matrix_from_input("first")
        matrix_b = get_matrix_from_input("second")
        result_matrix = multiply_matrices(matrix_a, matrix_b)
        if result_matrix is None:
            print("The operation cannot be performed.")
            print()
        else:
            print("The result is:")
            print_matrix(result_matrix)
            print()
    elif user_choice == 4:
        print()
        transpose_menu()
    return True


should_continue = True
while should_continue:
    should_continue = main_menu()

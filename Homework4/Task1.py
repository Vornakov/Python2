#  Задание No1
# 📌 Напишите функцию для транспонирования матрицы

def print_matrix(matrix: [[int]]) -> None:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()
    print()


def transpose_matrix(matrix: [[int]]) -> [[int]]:
    t_matrix = [[0] * len(matrix) for i in range(len(matrix[0]))]
    for i in range(len(t_matrix)):
        for j in range(len(t_matrix[0])):
            t_matrix[i][j] = matrix[j][i]
    return t_matrix


matrix_1 = [[1, 2, 3, 4],
            [5, 6, 7, 8]]
print_matrix(matrix_1)
print_matrix(transpose_matrix(matrix_1))

matrix_2 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
print_matrix(matrix_2)
print_matrix(transpose_matrix(matrix_2))
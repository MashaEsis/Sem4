from random import randint
import matplotlib.pyplot as plt
import time

def count_negative_cols(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    negative_cols = 0
    for j in range(cols):
        has_positive = False
        for i in range(rows):
            if matrix[i][j] >= 0:
                has_positive = True
                break
            if not has_positive:
                negative_cols += 1

    return negative_cols

def find_positive_row(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    positive_row = -1
    for i in range(rows):
        has_positive = False
        for j in range(cols):
            if matrix[i][j] > 0:
                has_positive = True
                break
        if has_positive:
            positive_row = i
            break

    return positive_row

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = [[0]*cols for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = randint(-10, 1)

for row in matrix:
    print(row)

negative_cols_count = count_negative_cols(matrix)
pozitiv_row_index = find_positive_row(matrix)
print("Количество столбцов, содержащих только отрицательные элементы:", negative_cols_count)
if pozitiv_row_index != -1:
    print("Номер первой строки, содержащей хотя бы 1 положительный элемент:", pozitiv_row_index)
else:
    print("Нет строк, содержащих положительный элемент")
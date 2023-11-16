def count_non_zero(matrix):
    if not matrix or not matrix[0]:
        return f'Матрица пуста или не содержит элементы.'
    rows = len(matrix)
    cols = len(matrix[0])
    non_zero = 0

    for i in range(rows):
        has_zero = False
        for j in range(cols):
            if matrix[i][j] == 0:
                has_zero = True
                break
        if not has_zero:
            non_zero += 1

    return non_zero


def input_matrix():
    while True:
        try:
            rows = int(input("Введите количество строк:"))
            cols = int(input("Введите количество столбцов:"))
            if rows <= 0 or cols <= 0:
                raise ValueError("Кол-во строк и стобцов должны быть положительными числами.")

            matrix = []
            for i in range(rows):
                row = []
                for j in range(cols):
                    element = int(input(f"Введите элемент матрицы [{i}], [{j}]:"))
                    row.append(element)
                matrix.append(row)
            return matrix
        except ValueError as e:
            print(f"Ошибка: {e}. Введите корректные значения:")


def print_matrix(matrix):
    print("Матрица:")
    for row in matrix:
        print(row)


matrix = input_matrix()
print_matrix(matrix)
result = count_non_zero(matrix)
print(f"Ненулевых строк: {result}")

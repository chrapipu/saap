while True:
    input_str = input("Введите целые числа, разделенные пробелами: ")

    # Разделение строки на отдельные числа, используя пробел как разделитель
    input_numbers = input_str.split()

    # Преобразование строки ввода в целые числа
    try:
        # Создание кортежа из преобразованных чисел
        my_tuple = tuple(map(int, input_numbers))

        # Инициализация переменной для хранения суммы положительных чисел
        positive_sum = 0

        # Проходим по элементам кортежа
        for num in my_tuple:
            # Проверяем, является ли число положительным
            if num > 0:
                # Если число положительное, добавляем его к сумме
                positive_sum += num

        # Выводим результат
        print("Сумма положительных элементов:", positive_sum)

        break  # Выход из цикла после успешного ввода и расчета

    except ValueError:
        print("Ошибка! Введите целые числа, разделенные пробелами.")

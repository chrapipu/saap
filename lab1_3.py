while True:
    try:
        # Запросите у пользователя ввод элементов списка, разделенных пробелом
        input_str = input("Введите элементы списка через пробел: ")

        # Разделите строку на элементы списка, используя пробел как разделитель
        elements = input_str.split()

        # Преобразуйте элементы в числа (предполагая, что пользователь вводит числа)
        input_list = [int(element) for element in elements]

        # Выход из бесконечного цикла, если корректный ввод
        break

    except ValueError:
        print("Ошибка! Введите только числа, разделенные пробелами.")

# Ваш код для выполнения задачи (найти наибольший четный элемент и преобразовать список)
max_even = None
for num in input_list:
    if num % 2 == 0 and (max_even is None or num > max_even):
        max_even = num

positive_elements = []
other_elements = []

for num in input_list:
    if num > 0:
        positive_elements.append(num)
    else:
        other_elements.append(num)

positive_elements.sort()

result_list = positive_elements + other_elements

if max_even is not None:
    print("Наибольший четный элемент:", max_even)
else:
    print("Четных элементов нет, выводим первый элемент списка:", input_list[0])

print("Преобразованный список:", result_list)

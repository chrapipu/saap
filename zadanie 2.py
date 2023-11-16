def function(data):
    if isinstance(data, dict):
        sorted_keys = sorted(data, key=data.get, reverse=True)
        three_keys = sorted_keys[:3]
        return f"Три ключа с самыми большими знасениями: {three_keys}"
    elif isinstance(data, list):
        numbers = [num for num in data if num % 2 == 0]
        unique_num = list(set(data))
        return f"Количество четных: {len(numbers)}. Список без повторений: {unique_num}."
    elif isinstance(data, int):
        digit_sum = sum(int(digit) for digit in str(abs(data)))
        return f"Сумма цифр числа:{digit_sum}."
    elif isinstance(data, str):
        cleaned_string = ''.join(char for char in data if char.isalnum() or char.isspace())
        count = len(cleaned_string.split())
        return f"Очищенная строка:{cleaned_string}, количество слов:{count}."

    else:
        return f"Тип данных не поддерживается."

def main ():
        user = input("Введите аргумент:")
        try:
            data = eval(user)
            result = function(data)
            print(result)
        except Exception as e:
            print(f"Ошибка: : {e}.")

if __name__=="__main__":
    main()
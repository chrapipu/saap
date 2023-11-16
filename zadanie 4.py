def div(a,b):
    try:
        res=a/b
        print(f"Результат:{res}")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль.")
    finally:
        print("деление :)")
a=int(input("Введите делимое число:"))
b=int(input("Введите делитель:"))
div(a,b)

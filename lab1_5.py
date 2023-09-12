# Исходный словарь с товарами в магазине
shop_items = {
    "молоко": [100, 10],
    "масло растительное": [200, 5],
    "яйца": [50, 20],
    "кофе": [300, 3],
    "творог": [150, 8]
}



# Функция для вывода цены товара
def print_price(item_name):
    if item_name in shop_items:
        print(f"{item_name} - {shop_items[item_name][0]}")
    else:
        print("Товар не найден")


# Функция для вывода количества товара
def print_quantity(item_name):
    if item_name in shop_items:
        print(f"{item_name} - {shop_items[item_name][1]}")
    else:
        print("Товар не найден")


# Функция для вывода всей информации о товарах в магазине
def print_all_info():
    print("Информация о товарах в магазине:")
    for item_name, item_info in shop_items.items():
        print(f"{item_name} - Цена: {item_info[0]}, Количество: {item_info[1]}")

# Функция для совершения покупки и вывода чека
def make_purchase():
    purchased_items = {}  # Создаем словарь для хранения купленных товаров

    total_cost = 0
    while True:
        item_name = input("Введите название товара (или 'n' для выхода): ")
        if item_name == 'n':
            break

        if item_name not in shop_items:
            print("Товар не найден")
            continue

        try:
            quantity = int(input(f"Введите количество {item_name}: "))
            if quantity <= 0:
                print("Количество должно быть положительным числом.")
                continue
        except ValueError:
            print("Введите корректное количество.")
            continue

        if quantity > shop_items[item_name][1]:
            print("Недостаточно товара в магазине.")
        else:
            cost = shop_items[item_name][0] * quantity
            total_cost += cost
            shop_items[item_name][1] -= quantity
            print(f"Вы добавили {item_name} x{quantity} к покупке. Сумма: {cost} руб.")

            # Добавляем купленный товар в чек
            purchased_items[item_name] = {'quantity': quantity, 'cost': cost}

    print(f"Итого к оплате: {total_cost} руб.")
    print("Чек:")
    for item_name, item_info in purchased_items.items():
        print(f"{item_name} - Количество: {item_info['quantity']}, Цена: {item_info['cost']} руб.")
    print("Остаток товаров в магазине:")
    print_all_info()



# Основной цикл программы
while True:
    print("\nМеню:")
    print("1. Просмотр цены")
    print("2. Просмотр количества")
    print("3. Вся информация")
    print("4. Покупка")
    print("5. До свидания")

    choice = input("Выберите пункт меню: ")

    if choice == '1':
        item_name = input("Введите название товара: ")
        print_price(item_name)
    elif choice == '2':
        item_name = input("Введите название товара: ")
        print_quantity(item_name)
    elif choice == '3':
        print_all_info()
    elif choice == '4':
        make_purchase()
    elif choice == '5':
        print("До свидания!")
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите пункт меню от 1 до 5.")

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

def filter_films_by_price(films, max_price):
    filtered_films = []
    for film in films:
        parts = film.rsplit(' ', 2)  # Split from the right, into three parts
        if len(parts) == 3 and parts[2].isdigit() and int(parts[2]) < max_price:
            filtered_films.append(film)
    return filtered_films

def filter_films_by_date(films, target_date):
    return [film for film in films if target_date in film]

def main():
    file_path = 'cinema.txt'  # Adjust the file path as needed
    films = read_file(file_path)

    # Фильтрация фильмов по цене
    cheap_films = filter_films_by_price(films, 15)
    if cheap_films:
        print("Фильмы со стоимостью билета меньше 15 рублей:")
        for film in cheap_films:
            print(film)
    else:
        print("Фильмы со стоимостью билета меньше 15 рублей не найдены.")

    # Ввод даты пользователем
    target_date = input("Введите дату для поиска фильмов (например, 12.07.2022): ")
    films_on_date = filter_films_by_date(films, target_date)
    if films_on_date:
        print(f"\nФильмы, показываемые {target_date}:")
        for film in films_on_date:
            print(film)
    else:
        print(f"Фильмы, показываемые на дату {target_date}, не найдены.")

if __name__ == "__main__":
    main()

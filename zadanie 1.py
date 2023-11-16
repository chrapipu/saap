def count(input_str):
    try:
        input_str = input_str.lower()
        glass = ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю']
        soglass = ['й', 'ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ф', 'в', 'п', 'р', 'л', 'д', 'ж', 'ч', 'с', 'м', 'т', 'б']

        count_of_glass = 0
        count_of_soglass = 0

        for char in input_str:
            if char in glass:
                count_of_glass += 1
            elif char in soglass:
                count_of_soglass += 1

        return count_of_glass, count_of_soglass

    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0


def main():
    try:
        input_str = input("Введите строку:")
        glass, soglass = count(input_str)
        print(f"Гласные: {glass} \nСогласные: {soglass}")
    except KeyboardInterrupt:
        print("\nOperation aborted by the user.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

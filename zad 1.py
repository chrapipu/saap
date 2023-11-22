def count_of_consonants(s):
    consonants = "йкнгшщзхждлрпвфчсмтб"
    count=0
    for char in s.lower():
        if char in consonants:
            count+=1
    return count

#Считывание данных и запись
with open('F1.txt','w+', encoding='utf-8') as f1:
    while True:
        user_input=input("Введите строку(оставьте пустую строку для завершения)")
        if user_input=="":
            break
        f1.write(user_input+'\n')
    f1.seek(0)
    print("f1:\n",f1.read())
    print("_---------------------")

#Чтение и запись в 2
with open('F1.txt', 'r', encoding='utf-8') as f1, open('F2.txt', 'w', encoding='utf-8') as f2:
    lines = f1.readlines()
    first_word = lines[0].split()[0] if lines else None
    for line in lines :
        if not any(word == first_word for word in line.split()):
            f2.write(line)

#Определение кол-ва согл букв в 1 строке 2
with open('F2.txt', 'r', encoding='utf-8') as f2:
    first_line = f2.readline()
    consonants_count = count_of_consonants(first_line)
    print(" F2:",f2.read())
print("--------------------------")
print(f"Количество согласных в первой строке F2: {consonants_count}")
def main(data):
    seen = set()
    result = []
    for row in data:
        if not any(cell is None for cell in row) and tuple(row) not in seen:
            seen.add(tuple(row))
            phone = ''.join(filter(str.isdigit, row[0]))
            email = row[1].replace('[at]', '@').split('@')[-1]
            date = '-'.join(row[2].split('/'))
            name = ' '.join([row[3].split()[0], row[3].split()[1][0] + '.'])
            result.append([phone, email, date, name])
    return result

# Пример использования:
table1 = [
    ["+7(155)971-35-14", "sarokij15[at]gmail.com", "1999/09/10", "Шарокий Б.Ф."],
    ["+7(665)891-01-58", "resanz44[at]rambler.ru", "2004/11/21", "Решянц О.Ц."],
    ["+7(665)891-01-58", "resanz44[at]rambler.ru", "2004/11/21", "Решянц О.Ц."],
    ["+7(882)167-79-34", "makovberg85[at]yandex.ru", "2000/08/12", "Маковберг И.С."],
    ["+7(962)515-46-02", "tosasko67[at]yandex.ru", "2002/11/22", "Тосаско М.У."]
]

table2 = [
    ["+7(207)932-82-69", "visugak86[at]gmail.com", "2000/04/01", "Висугяк Г.О."],
    ["+7(969)154-14-47", "debic68[at]mail.ru", "2003/07/16", "Дебич О.Е."],
    ["+7(969)154-14-47", "debic68[at]mail.ru", "2003/07/16", "Дебич О.Е."],
    ["+7(511)932-24-72", "situk91[at]yandex.ru", "2003/02/10", "Ситук Г.Е."]
]

# Преобразуем таблицы
transformed_table1 = main(table1)
transformed_table2 = main(table2)

# Выводим результаты
for row in transformed_table1:
    print(row)

print()

for row in transformed_table2:
    print(row)

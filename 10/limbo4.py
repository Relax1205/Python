import re
from datetime import datetime


def remove_duplicates_and_empty_rows(table):
    # Убираем дубликаты через set(), а затем фильтруем пустые строки
    unique_rows = list(set(tuple(row) for row in table))
    return list(
        filter(
            lambda row: any(cell is not None and cell != '' for cell in row),
            unique_rows
        )
    )


def transform_phone(cell):
    return re.sub(r'\D', '', cell)[1:]


def transform_email(cell):
    if '[at]' in cell:
        cell = cell.replace('[at]', '@')
    if '@' in cell:
        return cell.split('@')[1]
    return None


def transform_date(cell):
    try:
        return datetime.strptime(cell, "%Y/%m/%d").strftime("%Y-%m-%d")
    except ValueError:
        return None


def transform_name(cell):
    if cell:
        parts = cell.split()
        if len(parts) >= 2:
            return f"{parts[0]} {parts[1][0]}."
    return None


def transform_cell(cell, column):
    if cell is None:
        return None
    if column == 1:
        return transform_phone(cell)
    elif column == 2:
        return transform_email(cell)
    elif column == 3:
        return transform_date(cell)
    elif column == 4:
        return transform_name(cell)
    return cell


def main(table):
    # Убираем дубликаты и пустые строки
    table = remove_duplicates_and_empty_rows(table)
    
    # Преобразуем каждую строку таблицы
    transformed_table = list(
        map(
            lambda row: list(
                map(
                    lambda i_cell: transform_cell(i_cell[1], i_cell[0] + 1),
                    enumerate(row)
                )
            ),
            table
        )
    )
    
    return transformed_table


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
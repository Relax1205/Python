import re
from datetime import datetime

def remove_none_columns(table):
    empty_columns = [i for i, column in enumerate(table[0])
                     if all(row[i] is None for row in table)]

    for column_index in reversed(empty_columns):
        for row in table:
            del row[column_index]

    return table


def remove_duplicated_rows(table):
    unique_rows = []
    seen_rows = set()
    for row in table:
        row_tuple = tuple(row)
        if row_tuple not in seen_rows:
            unique_rows.append(row)
            seen_rows.add(row_tuple)
    return unique_rows


def remove_none_rows(table):
    return [row for row in table if not all(value is None for value in row)]


def transform_phone(cell):
    return re.sub(r'\D', '', cell)[1:] if cell else None


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
    if column == 1:
        return transform_phone(cell)
    elif column == 2:
        return transform_email(cell)
    elif column == 3:
        return transform_date(cell)
    elif column == 4:
        return transform_name(cell)
    return cell


def format_data(table):
    for row in table:
        for i, cell in enumerate(row):
            row[i] = transform_cell(cell, i + 1)
    return table


def main(table):
    arr = [row[:] for row in table]
    arr = remove_none_columns(arr)
    arr = remove_duplicated_rows(arr)
    arr = remove_none_rows(arr)
    arr = format_data(arr)
    return arr


table = [
    ['+7(155)971-35-14', 'sarokij15[at]gmail.com', '1999/09/10', 'Шарокий Б.Ф.'],
    ['+7(665)891-01-58', 'resanz44[at]rambler.ru', '2004/11/21', 'Решянц О.Ц.'],
    ['+7(665)891-01-58', 'resanz44[at]rambler.ru', '2004/11/21', 'Решянц О.Ц.'],
    ['+7(882)167-79-34', 'makovberg85[at]yandex.ru', '2000/08/12', 'Маковберг И.С.'],
    ['+7(962)515-46-02', 'tosasko67[at]yandex.ru', '2002/11/22', 'Тосаско М.У.'],
    ['+7(207)932-82-69', 'visugak86[at]gmail.com', '2000/04/01', 'Висугяк Г.О.'],
    ['+7(969)154-14-47', 'debic68[at]mail.ru', '2003/07/16', 'Дебич О.Е.'],
    ['+7(969)154-14-47', 'debic68[at]mail.ru', '2003/07/16', 'Дебич О.Е.'],
    ['+7(511)932-24-72', 'situk91[at]yandex.ru', '2003/02/10', 'Ситук Г.Е.']
]

result = main(table)

# Выводим результат в нужном формате
for row in result:
    print(row)

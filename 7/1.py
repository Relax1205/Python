def zero(items, java_case, eagle_case, oz_case):
    item = items[0].lower() if isinstance(items[0], str) else items[0]
    if item == 'java':
        return java_case
    elif item == 'eagle':
        return eagle_case
    elif item == 'oz':
        return oz_case


def two(items, case_2001, case_2018, case_2019):
    if items[2] == 2001:
        return case_2001
    elif items[2] == 2018:
        return case_2018
    elif items[2] == 2019:
        return case_2019


def three(items, case_2005, case_2003, case_1977):
    if items[3] == 2005:
        return case_2005
    elif items[3] == 2003:
        return case_2003
    elif items[3] == 1977:
        return case_1977


def zero_arc(items, java_case, eagle_case, oz_case):
    item = items[0].lower() if isinstance(items[0], str) else items[0]
    if item == 'java':
        return java_case
    elif item == 'eagle':
        return eagle_case
    elif item == 'oz':
        return oz_case


def one(items, gdb_case, mirah_case, arc_case):
    item = items[1].lower() if isinstance(items[1], str) else items[1]
    if item == 'gdb':
        return gdb_case
    elif item == 'mirah':
        return mirah_case
    elif item == 'arc':
        return arc_case


def main(items):
    return one(
        items,
        5,
        two(
            items,
            zero(items, 0, 1, 2),
            3,
            4
        ),
        zero_arc(
            items,
            three(items, 6, 7, 8),
            9,
            10
        )
    )





# Примеры вычислений
print(main(['OZ', 'GDB', 2018, 2005]))  # 5
print(main(['EAGLE', 'ARC', 2018, 1977]))  # 9
print(main(['EAGLE', 'MIRAH', 2019, 2005]))  # 4
print(main(['JAVA', 'MIRAH', 2018, 2005]))  # 3
print(main(['JAVA', 'ARC', 2001, 2005]))  # 6

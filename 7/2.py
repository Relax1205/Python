def zero(items, java_case, eagle_case, oz_case):
    mapping = {
        'java': java_case,
        'eagle': eagle_case,
        'oz': oz_case
    }
    item = items[0].lower() if isinstance(items[0], str) else items[0]
    return mapping.get(item, None)


def two(items, case_2001, case_2018, case_2019):
    mapping = {
        2001: case_2001,
        2018: case_2018,
        2019: case_2019
    }
    return mapping.get(items[2], None)


def three(items, case_2005, case_2003, case_1977):
    mapping = {
        2005: case_2005,
        2003: case_2003,
        1977: case_1977
    }
    return mapping.get(items[3], None)


def zero_arc(items, java_case, eagle_case, oz_case):
    mapping = {
        'java': java_case,
        'eagle': eagle_case,
        'oz': oz_case
    }
    item = items[0].lower() if isinstance(items[0], str) else items[0]
    return mapping.get(item, None)


def one(items, gdb_case, mirah_case, arc_case):
    mapping = {
        'gdb': gdb_case,
        'mirah': mirah_case,
        'arc': arc_case
    }
    item = items[1].lower() if isinstance(items[1], str) else items[1]
    return mapping.get(item, None)


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

# Тестовые примеры
print(main(['OZ', 'GDB', 2018, 2005]))        # 5
print(main(['EAGLE', 'ARC', 2018, 1977]))     # 9
print(main(['EAGLE', 'MIRAH', 2019, 2005]))   # 4
print(main(['JAVA', 'MIRAH', 2018, 2005]))    # 3
print(main(['JAVA', 'ARC', 2001, 2005]))      # 6
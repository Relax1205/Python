def main(items):
    items = [x.lower() if isinstance(x, str) else x for x in items]
    
    zero_dict = {"java": 0, "eagle": 1, "oz": 2}
    two_dict = {2001: zero_dict.get(items[0], -1), 2018: 3, 2019: 4}
    three_dict = {2005: 6, 2003: 7, 1977: 8}
    zero_arc_dict = {
        "java": three_dict.get(items[3], -1), "eagle": 9, "oz": 10}
    one_dict = {
        "gdb": 5, "mirah": two_dict.get(items[2], -1),
        "arc": zero_arc_dict.get(items[0], -1)
    }

    return one_dict.get(items[1], -1)


# Примеры вычислений
print(main(['OZ', 'GDB', 2018, 2005]))  # 5
print(main(['EAGLE', 'ARC', 2018, 1977]))  # 9
print(main(['EAGLE', 'MIRAH', 2019, 2005]))  # 4
print(main(['JAVA', 'MIRAH', 2018, 2005]))  # 3
print(main(['JAVA', 'ARC', 2001, 2005]))  # 6

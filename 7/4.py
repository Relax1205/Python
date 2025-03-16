s = [
    {(1, 'mirah'), (2, 2001), (0, 'java')},
    {(1, 'mirah'), (2, 2001), (0, 'eagle')},
    {(1, 'mirah'), (2, 2001), (0, 'oz')},
    {(1, 'mirah'), (2, 2018)},
    {(1, 'mirah'), (2, 2019)},
    {(1, 'gdb')},
    {(1, 'arc'), (0, 'java'), (3, 2005)},
    {(1, 'arc'), (0, 'java'), (3, 2003)},
    {(1, 'arc'), (0, 'java'), (3, 1977)},
    {(1, 'arc'), (0, 'eagle')},
    {(1, 'arc'), (0, 'oz')}
]

def main(r):
    input_set = set()
    for idx, val in enumerate(r):
        normalized_val = val.lower() if isinstance(val, str) else val
        input_set.add((idx, normalized_val))
    for index, subset in enumerate(s):
        if subset.issubset(input_set):
            return index
    return -1

# Примеры вычислений
print(main(['OZ', 'GDB', 2018, 2005]))  # 5
print(main(['EAGLE', 'ARC', 2018, 1977]))  # 9
print(main(['EAGLE', 'MIRAH', 2019, 2005]))  # 4
print(main(['JAVA', 'MIRAH', 2018, 2005]))  # 3
print(main(['JAVA', 'ARC', 2001, 2005]))  # 6

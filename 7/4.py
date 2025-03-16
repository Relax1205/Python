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
    input_set = {(idx, val.lower() if isinstance(val, str) else val) for idx, val in enumerate(r)}
    matching_indices = [i for i in range(len(s)) if s[i].issubset(input_set)]
    return matching_indices[0] if matching_indices else -1

# Example calls to the main function
result1 = main(['OZ', 'GDB', 2018, 2005])
result2 = main(['EAGLE', 'ARC', 2018, 1977])
result3 = main(['EAGLE', 'MIRAH', 2019, 2005])
result4 = main(['JAVA', 'MIRAH', 2018, 2005])
result5 = main(['JAVA', 'ARC', 2001, 2005])
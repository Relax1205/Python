class Subset:
    def __init__(self, index, elements):
        self.index = index
        self.elements = elements

    def is_subset(self, input_set):
        return all(elem in input_set for elem in self.elements)


subsets = [
    Subset(0, [(1, 'mirah'), (2, 2001), (0, 'java')]),
    Subset(1, [(1, 'mirah'), (2, 2001), (0, 'eagle')]),
    Subset(2, [(1, 'mirah'), (2, 2001), (0, 'oz')]),
    Subset(3, [(1, 'mirah'), (2, 2018)]),
    Subset(4, [(1, 'mirah'), (2, 2019)]),
    Subset(5, [(1, 'gdb')]),
    Subset(6, [(1, 'arc'), (0, 'java'), (3, 2005)]),
    Subset(7, [(1, 'arc'), (0, 'java'), (3, 2003)]),
    Subset(8, [(1, 'arc'), (0, 'java'), (3, 1977)]),
    Subset(9, [(1, 'arc'), (0, 'eagle')]),
    Subset(10, [(1, 'arc'), (0, 'oz')])
]


def normalize_input(r):
    return {
        (idx, val.lower() if isinstance(val, str) else val)
        for idx, val in enumerate(r)
    }


def find_subset_index(input_set):
    for subset in subsets:
        if subset.is_subset(input_set):
            return subset.index
    return -1


def main(r):
    input_set = normalize_input(r)
    return find_subset_index(input_set)


# Примеры вычислений
print(main(['OZ', 'GDB', 2018, 2005]))  # 5
print(main(['EAGLE', 'ARC', 2018, 1977]))  # 9
print(main(['EAGLE', 'MIRAH', 2019, 2005]))  # 4
print(main(['JAVA', 'MIRAH', 2018, 2005]))  # 3
print(main(['JAVA', 'ARC', 2001, 2005]))  # 6

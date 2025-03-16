class Tree:
    def __init__(self, number, top, topcon, mid, midcon, down, downcon):
        self.number = number
        self.cases = [
            (top, topcon),
            (mid, midcon),
            (down, downcon)
        ]

    def find(self, mas):
        if self.number >= len(mas):
            return -1
        current_value = mas[self.number]
        for expected_value, consequence in self.cases:
            if current_value == expected_value:
                return self._process_consequence(consequence, mas)
        return -1

    def _process_consequence(self, consequence, mas):
        if isinstance(consequence, int):
            return consequence
        return consequence.find(mas)


def main(mas):
    normalized_mas = [
        x.lower() if isinstance(x, str) else x
        for x in mas
    ]
    java_3_node = Tree(
        3, 2005, 6, 2003, 7, 1977, 8
    )
    arc_0_node = Tree(
        0, "java", java_3_node, "eagle", 9, "oz", 10
    )
    mirah_0_node = Tree(
        0, "java", 0, "eagle", 1, "oz", 2
    )
    mirah_2_node = Tree(
        2, 2001, mirah_0_node, 2018, 3, 2019, 4
    )
    root = Tree(
        1, "gdb", 5, "arc", arc_0_node, "mirah", mirah_2_node
    )
    return root.find(normalized_mas)

# Примеры вычислений
print(main(['OZ', 'GDB', 2018, 2005]))  # 5
print(main(['EAGLE', 'ARC', 2018, 1977]))  # 9
print(main(['EAGLE', 'MIRAH', 2019, 2005]))  # 4
print(main(['JAVA', 'MIRAH', 2018, 2005]))  # 3
print(main(['JAVA', 'ARC', 2001, 2005]))  # 6

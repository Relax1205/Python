def handle_MIRAH(items):
    match items[2]:
        case 2001:
            match items[0].lower():
                case 'java':
                    return 0
                case 'eagle':
                    return 1
                case 'oz':
                    return 2
                case _:
                    print(f"Unexpected value for items[0]: {items[0]}")
                    return None
        case 2018:
            return 3
        case 2019:
            return 4
        case _:
            print(f"Unexpected value for items[2]: {items[2]}")
            return None


def handle_GDB():
    return 5


def handle_ARC(items):
    match items[0].lower():
        case 'java':
            match items[3]:
                case 2005:
                    return 6
                case 2003:
                    return 7
                case 1977:
                    return 8
                case _:
                    print(f"Unexpected value for items[3]: {items[3]}")
                    return None
        case 'eagle':
            return 9
        case 'oz':
            return 10
        case _:
            print(f"Unexpected value for items[0]: {items[0]}")
            return None


def main(items):
    match items[1].lower():
        case 'mirah':
            return handle_MIRAH(items)
        case 'gdb':
            return handle_GDB()
        case 'arc':
            return handle_ARC(items)
        case _:
            print(f"Unexpected value for items[1]: {items[1]}")
            return None


# Тестовые примеры
print(main(['OZ', 'GDB', 2018, 2005]))        # 5
print(main(['EAGLE', 'ARC', 2018, 1977]))     # 9
print(main(['EAGLE', 'MIRAH', 2019, 2005]))   # 4
print(main(['JAVA', 'MIRAH', 2018, 2005]))    # 3
print(main(['JAVA', 'ARC', 2001, 2005]))      # 6
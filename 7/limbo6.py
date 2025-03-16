def handle_MIRAH_2001_Java():
    return 0


def handle_MIRAH_2001_Eagle():
    return 1


def handle_MIRAH_2001_OZ():
    return 2


def handle_MIRAH_2001(items):
    match items[0].lower():
        case 'java':
            return handle_MIRAH_2001_Java()
        case 'eagle':
            return handle_MIRAH_2001_Eagle()
        case 'oz':
            return handle_MIRAH_2001_OZ()
        case _:
            return None


def handle_MIRAH_2018():
    return 3


def handle_MIRAH_2019():
    return 4


def handle_MIRAH(items):
    match items[2]:
        case 2001:
            return handle_MIRAH_2001(items)
        case 2018:
            return handle_MIRAH_2018()
        case 2019:
            return handle_MIRAH_2019()
        case _:
            return None


def handle_GDB():
    return 5


def handle_ARC_Java_2005():
    return 6


def handle_ARC_Java_2003():
    return 7


def handle_ARC_Java_1977():
    return 8


def handle_ARC_Java(items):
    match items[3]:
        case 2005:
            return handle_ARC_Java_2005()
        case 2003:
            return handle_ARC_Java_2003()
        case 1977:
            return handle_ARC_Java_1977()
        case _:
            return None


def handle_ARC_Eagle():
    return 9


def handle_ARC_OZ():
    return 10


def handle_ARC(items):
    match items[0].lower():
        case 'java':
            return handle_ARC_Java(items)
        case 'eagle':
            return handle_ARC_Eagle()
        case 'oz':
            return handle_ARC_OZ()
        case _:
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
            return None

# Тестовые примеры
print(main(['OZ', 'GDB', 2018, 2005]))        # 5
print(main(['EAGLE', 'ARC', 2018, 1977]))     # 9
print(main(['EAGLE', 'MIRAH', 2019, 2005]))   # 4
print(main(['JAVA', 'MIRAH', 2018, 2005]))    # 3
print(main(['JAVA', 'ARC', 2001, 2005]))      # 6
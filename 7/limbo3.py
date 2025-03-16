def create_rules():
    return {
        'gdb': lambda n: 5,
        'mirah': {
            2001: {'java': 0, 'eagle': 1, 'oz': 2},
            2018: 3,
            2019: 4
        },
        'arc': {
            'java': {2005: 6, 2003: 7, 1977: 8},
            'eagle': 9,
            'oz': 10
        }
    }


def normalize(items):
    return [x.lower() if isinstance(x, str) else x for x in items]


def process_mirah(rules, normalized):
    year_data = rules['mirah'].get(normalized[2], {})
    return year_data.get(normalized[0], -1) if isinstance(year_data, dict) else year_data


def process_arc(rules, normalized):
    lang_data = rules['arc'].get(normalized[0], -1)
    if normalized[0] == 'java':
        return lang_data.get(normalized[3], -1)
    return lang_data


def main(items):
    normalized = normalize(items)
    rules = create_rules()
    key = normalized[1]
    if key not in rules:
        return -1
    if key == 'gdb':
        return rules[key](normalized)
    if key == 'mirah':
        return process_mirah(rules, normalized)
    if key == 'arc':
        return process_arc(rules, normalized)
    return -1


# Примеры вычислений
print(main(['OZ', 'GDB', 2018, 2005]))  # 5
print(main(['EAGLE', 'ARC', 2018, 1977]))  # 9
print(main(['EAGLE', 'MIRAH', 2019, 2005]))  # 4
print(main(['JAVA', 'MIRAH', 2018, 2005]))  # 3
print(main(['JAVA', 'ARC', 2001, 2005]))  # 6

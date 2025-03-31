def main(input_string):
    content = input_string.strip()
    if not is_valid_structure(content):
        return []
    inner_content = extract_inner_content(content)
    blocks = split_into_blocks(inner_content)
    return [parse_block(block) for block in blocks if parse_block(block)]


def is_valid_structure(content):
    return content.startswith('.do') and content.endswith('.end')


def extract_inner_content(content):
    return content[3:-4].strip()


def split_into_blocks(inner_content):
    blocks = []
    for part in inner_content.split('||'):
        cleaned = part.strip().rstrip('.')
        if cleaned:
            blocks.append(cleaned)
    return blocks


def parse_block(block):
    block = block.strip()
    if not block.startswith('define'):
        return None
    if '->' not in block:
        return None
    name_part, value_part = block.split('->', 1)
    name = name_part[len('define'):].strip()
    value_part = value_part.strip()
    if not (value_part.startswith('q(') and value_part.endswith(')')):
        return None
    return (value_part[2:-1], name)

# Примеры использования
input_str1 = """.do || define teer -> q(rixequ). ||. ||define rele -> q(gera_308).||..end"""
print(main(input_str1))  # [('rixequ', 'teer'), ('gera_308', 'rele')]

input_str2 = """.do || define usla -> q(zaatre). ||. || define esxea -> q(oned_46).||.|| define anusin_937 -> q(tece_581). ||. .end"""
print(main(input_str2))  # [('zaatre', 'usla'), ('oned_46', 'esxea'), ('tece_581', 'anusin_937')]
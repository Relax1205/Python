import re
from datetime import datetime


def clean_table(table):
    seen = set()
    unique_rows = []
    for row in table:
        row_tuple = tuple(row)
        if row_tuple not in seen and any(cell for cell in row if cell):
            seen.add(row_tuple)
            unique_rows.append(row)
    return unique_rows


def transform_phone(phone):
    digits = re.sub(r'\D', '', phone)
    return digits[1:] if digits else None


def transform_email(email):
    email = email.replace('[at]', '@')
    parts = email.split('@')
    return parts[1] if len(parts) > 1 else None


def transform_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y/%m/%d")
        return date_obj.strftime("%Y-%m-%d")
    except (ValueError, TypeError):
        return None


def transform_name(name):
    if not name:
        return None
    parts = name.split()
    if len(parts) >= 2 and len(parts[1]) > 0:
        return f"{parts[0]} {parts[1][0]}."
    return name


transformations = {
    0: transform_phone,
    1: transform_email,
    2: transform_date,
    3: transform_name
}


def process_table(table):
    cleaned = clean_table(table)
    return [
        [
            transformations.get(col_idx, lambda x: x)(cell)
            for col_idx, cell in enumerate(row)
        ]
        for row in cleaned
    ]

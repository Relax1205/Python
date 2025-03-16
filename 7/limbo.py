def handle_mirah_case(normalized):
    cases_2001 = {'java': 0, 'eagle': 1, 'oz': 2}
    cases_other = {2018: 3, 2019: 4}
    return (
        cases_2001.get(normalized[0], -1) 
        if normalized[2] == 2001 
        else cases_other.get(normalized[2], -1)
    )

def handle_arc_case(normalized):
    if normalized[0] == 'java':
        return {2005: 6, 2003: 7, 1977: 8}.get(normalized[3], -1)
    return {'eagle': 9, 'oz': 10}.get(normalized[0], -1)

def main(items):
    normalized = [
        x.lower() if isinstance(x, str) else x 
        for x in items
    ]
    handlers = {
        'gdb': lambda _: 5,
        'mirah': handle_mirah_case,
        'arc': handle_arc_case
    }
    return handlers.get(normalized[1], lambda _: -1)(normalized)

# --- Тесты ---
print(main(['OZ', 'GDB', 2018, 2005]))        # 5
print(main(['EAGLE', 'ARC', 2018, 1977]))     # 9
print(main(['EAGLE', 'MIRAH', 2019, 2005]))   # 4
print(main(['JAVA', 'MIRAH', 2018, 2005]))    # 3
print(main(['JAVA', 'ARC', 2001, 2005]))      # 6
def main(value: int):
    shifts_and_masks = [
        (0, 0b111111),
        (6, 0b111111),
        (12, 0b1111111),
        (19, 0b1111),
        (23, 0b1)
    ]
    return tuple(
        map(
            lambda sm: hex((value >> sm[0]) & sm[1]),
            shifts_and_masks
        )
    )

print(main(9116495))  # ('0xf', '0x2d', '0x31', '0x1', '0x1')
print(main(4986078))  # ('0x1e', '0x13', '0x41', '0x9', '0x0')
print(main(16396824))  # ('0x18', '0x8', '0x23', '0xf', '0x1')
print(main(12431249))  # ('0x11', '0x3e', '0x5a', '0x7', '0x1')
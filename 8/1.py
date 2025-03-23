def main(value: int):
    I1 = value & 0b111111
    I2 = (value >> 6) & 0b111111
    I3 = (value >> 12) & 0b1111111
    I4 = (value >> 19) & 0b1111
    I5 = (value >> 23) & 0b1
    return (
        hex(I1),
        hex(I2),
        hex(I3),
        hex(I4),
        hex(I5)
    )


# Тесты
if __name__ == "__main__":
    print(main(9116495))  # ('0xf', '0x2d', '0x31', '0x1', '0x1')
    print(main(4986078))  # ('0x1e', '0x13', '0x41', '0x9', '0x0')
    print(main(16396824))  # ('0x18', '0x8', '0x23', '0xf', '0x1')
    print(main(12431249))  # ('0x11', '0x3e', '0x5a', '0x7', '0x1')
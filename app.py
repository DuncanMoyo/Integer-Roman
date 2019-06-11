# Convert Integer to Roman Numerals
# Dictionary not too effective for me, two lists worked better
def int_to_rom(number):
    value = [
        1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
    ]

    symbol = [
        'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'
    ]

    roman_numeral = ''
    i = 0
    while number > 0:
        for _ in range(num // value[i]):
            roman_numeral += symbol[i]
            number -= val[i]
        i += 1
    return roman_numeral


print(int_to_rom(#your_number))

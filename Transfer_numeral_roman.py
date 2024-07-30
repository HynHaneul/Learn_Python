class RomanNumeralConverter:
    def __init__(self):
        self.roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        self.roman_order = ["M" , "D", "C" , "L", "X", "V", "I"]
    def roman_to_int (self, roman_numeral):
        result = 0
        pre_value = 0

        for char in roman_numeral[::-1]:
            value = self.roman_values[char]
            if value < pre_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result
    def int_to_roman (self, num):
        roman_numeral = ""
        for symbol in self.roman_order:
            count = int(num/self.roman_values[symbol])
            roman_numeral += (symbol * count)
            num -= self.roman_values[symbol] * count
        return roman_numeral
def main():
    converter = RomanNumeralConverter()
    #convert to roman number to decimal
    print (converter.roman_to_int(("MCMXCIV"))) # output: 1994

    #convert to decial number to roman
    print(converter.int_to_roman(2023)) # Output: MMXXIII
if __name__ == "__main__":
    main()



"""def soar_to_roman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_numeral = ""
    for i, v in enumerate(values):
        count = int(num / v)
        roman_numeral += (numerals[i] * count)
        num -= v * count
    return roman_numeral

# Ví dụ sử dụng
print(soar_to_roman(42))  # Output: XLII
print(soar_to_roman(4))   # Output: IV
print(soar_to_roman(14))  # Output: XIV
print(soar_to_roman(1994)) # Output: MCMXCIV


def roman_to_int(s):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev_value = 0

    for char in s[::-1]:
        value = roman_values[char]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result

print(roman_to_int('III'))  # Output: 3
print(roman_to_int('IV'))  # Output: 4
print(roman_to_int('IX'))  # Output: 9
print(roman_to_int('LVIII'))  # Output: 58
print(roman_to_int('MCMXCIV'))  # Output: 1994

"""
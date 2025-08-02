class IntegerToRoman:
    def __init__(self, number):
        if not (1 <= number <= 3999):
            raise ValueError("Number must be between 1 and 3999")
        self.number = number

    def convert(self):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        num = self.number
        roman = ""

        for i in range(len(val)):
            count = num // val[i]
            roman += syms[i] * count
            num -= val[i] * count

        return roman

# Example usage
number = 1987
converter = IntegerToRoman(number)
print(f"Integer: {number}")
print("Roman Numeral:", converter.convert())

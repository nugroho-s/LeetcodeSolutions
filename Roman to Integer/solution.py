class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        last_int = 0
        for c in s[::-1]:
            int_val = roman_map[c]
            if int_val >= last_int:
                sum = sum + int_val
                last_int = int_val
            else:
                sum = sum - int_val

        return sum
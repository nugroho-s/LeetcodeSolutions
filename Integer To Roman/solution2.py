class Solution:
    int_roman_map = {
        1 : 'I',
        4 : 'IV',
        5 : 'V',
        9 : 'IX',
        10 : 'X',
        40: 'XL',
        50 : 'L',
        90 : 'XC',
        100 : 'C',
        400 : 'CD',
        500 : 'D',
        900 : 'CM',
        1000 : 'M'
    }
    def intToRoman(self, num: int) -> str:
        sorted_keys = list(self.int_roman_map.keys())
        sorted_keys.sort(reverse=True)
        roman = ""
        for key in sorted_keys:
            while num - key >= 0:
                num -= key
                roman += self.int_roman_map[key]
        return roman

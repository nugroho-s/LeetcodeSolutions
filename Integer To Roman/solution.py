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
        while num > 0:
            idx = next(x for x in sorted_keys if x <= num)
            roman += self.int_roman_map[idx]
            num -= idx
        return roman

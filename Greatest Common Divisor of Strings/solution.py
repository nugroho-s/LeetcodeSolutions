class Solution:
    def checkDivisor(self, str1: str, divisor: str) -> bool:
        len_div = len(divisor)
        if len(str1) % len_div is not 0:
            return False
        i = 0
        while i < len(str1):
            if str1[i:i+len_div] != divisor:
                return False
            i += len_div
        return True

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_str = str1 if len(str1) < len(str2) else str2
        for i in range(len(min_str), 0, -1):
            if self.checkDivisor(str1, min_str[:i]) and self.checkDivisor(str2, min_str[:i]):
                return min_str[:i]
        return ""

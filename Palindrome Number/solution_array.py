import math

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        digits = []
        while x > 0:
            digits.append(x % 10)
            x = x // 10
        if (not digits and x < 0):
            return False
        for i in range(len(digits)):
            if (digits[i] != digits[-(i+1)]):
                return False
        return True
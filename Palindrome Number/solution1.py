import math

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        digits = int(math.log(x,10)) + 1
        for i in range(1, (digits/2) + 1):
            d1 = x // (10**(digits - i)) % 10
            d2 = x % (10**i)  // (10**(i-1))
            if d1 != d2:
                return False

        return True
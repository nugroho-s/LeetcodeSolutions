class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        upper_a = int(sqrt(c))+1
        for a in range(upper_a):
            b = int(sqrt(c - a**2))
            if a**2 + b**2 == c:
                return True
        return False

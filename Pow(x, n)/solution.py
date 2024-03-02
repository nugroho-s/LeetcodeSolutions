class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (n == 0):
            return 1
        if (n == 1):
            return x
        if (n == -1):
            return 1/x
        else:
            return self.myPowMemo(x, n, {})

    def myPowMemo(self, x: float, n: int, memo = {}) -> float:
        if n in memo:
            return memo[n]
        if (n == 0):
            return 1
        if (n == 1):
            return x
        if (n == -1):
            return 1/x
        else:
            n1 = n // 2
            n2 = n - n1
            pn1 = self.myPowMemo(x, n1, memo)
            memo[n1] = pn1 
            if n1 == n2:
                return pn1 * pn1
            pn2 = self.myPowMemo(x, n2, memo)
            memo[n2] = pn2
            return pn1 * pn2

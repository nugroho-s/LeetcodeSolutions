class Solution:
    def climbStairs(self, n: int, memo = {}) -> int:
        if n in memo:
            return memo[n]
        if n<=1:
            return 1
        n1 = self.climbStairs(n-1)
        memo[n-1] = n1
        n2 = self.climbStairs(n-2)
        memo[n-2] = n2
        return n1 + n2

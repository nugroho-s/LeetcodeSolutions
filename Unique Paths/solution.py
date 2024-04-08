class Solution:
    def uniquePaths(self, m: int, n: int, memo = {}) -> int:
        if m is 1:
            return 1
        if n is 1:
            return 1
        if m is 2 and n is 2:
            return 2
        if tuple([m,n]) in memo:
            return memo[tuple([m,n])]
        if tuple([n,m]) in memo:
            return memo[tuple([n,m])]
        right_path = self.uniquePaths(m, n - 1)
        memo[tuple([m, n - 1])] = right_path
        down_path = self.uniquePaths(m-1, n)
        memo[tuple([m - 1, n])] = down_path
        return right_path + down_path

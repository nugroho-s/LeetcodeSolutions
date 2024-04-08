class Solution:
    def uniquePaths(self, m: int, n: int, memo = {}) -> int:
        if m is 1:
            return 1
        if n is 1:
            return 1
        if m is 2 and n is 2:
            return 2
        # get value from memo if it exists
        # uniquePaths(m, n) = uniquePaths(n,m)
        if tuple([m,n]) in memo:
            return memo[tuple([m,n])]
        if tuple([n,m]) in memo:
            return memo[tuple([n,m])]
        # uniquePaths(m, n) = uniquePaths(m-1, n) + uniquePaths(m, n-1)
        right_path = self.uniquePaths(m, n - 1)
        memo[tuple([m, n - 1])] = right_path
        down_path = self.uniquePaths(m-1, n)
        memo[tuple([m - 1, n])] = down_path
        return right_path + down_path

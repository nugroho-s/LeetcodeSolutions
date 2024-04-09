class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.minPathSumRec(grid, 0, 0, {})
        
    # storing memo in separate function since somehow previous memo is not being passed in recursive calls
    def minPathSumRec(self, grid: List[List[int]], i, j, memo) -> int:
        if tuple([i,j]) in memo:
            return memo[tuple([i,j])]
        if len(grid) - i is 1:
            result = sum(grid[len(grid) - 1][j:])
            memo[tuple([i,j])] = result
            return result
        if len(grid[0]) - j is 1:
            total = 0
            for row in grid[i:]:
                total += row[len(grid[0]) - 1]
            memo[tuple([i,j])] = total
            return total
        right = grid[i][j] + self.minPathSumRec(grid, i, j+1, memo)
        down = grid[i][j] + self.minPathSumRec(grid, i+1, j, memo)
        min_path = min(right, down)
        memo[tuple([i,j])] = min_path
        return min_path

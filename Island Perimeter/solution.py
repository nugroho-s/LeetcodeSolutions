class Solution:
    def checkNeighbor(self, grid: List[List[int]], i, j) -> int:
        if i < 0 or i >= len(grid):
            return 1
        if j < 0 or j >= len(grid[i]):
            return 1
        return not grid[i][j]

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    perimeter += (self.checkNeighbor(grid, i-1, j) + self.checkNeighbor(grid, i+1, j) + 
                    self.checkNeighbor(grid, i, j-1) + self.checkNeighbor(grid, i, j+1))
        return perimeter

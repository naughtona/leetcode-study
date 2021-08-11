from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.N_ROWS, self.N_COLS = len(grid), len(grid[0])
        n_islands = 0

        for i in range(self.N_ROWS):
            for j in range(self.N_COLS):
                if grid[i][j]) == "1":
                    self.dfs(i, j, grid)
                    n_islands += 1
        
        return n_islands

    def dfs(self, row: int, col: int, grid: List[List[str]]) -> int:
        stack = [(row,col)]

        while stack:
            i, j = stack.pop()
            grid[i][j] = "0"
            # top
            if i-1 >= 0 and grid[i-1][j] == "1":
                stack += [(i-1,j)]
            # bottom
            if i+1 < self.N_ROWS and grid[i+1][j] == "1":
                stack += [(i+1,j)]
            # left
            if j-1 >= 0 and grid[i][j-1] == "1":
                stack += [(i,j-1)]
            # right
            if j+1 < self.N_COLS and grid[i][j+1] == "1":
                stack += [(i,j+1)]
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid); COLUMNS = len(grid[0]) 

        def markIt_dfs(mat, r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLUMNS or mat[r][c] == "0":
                return 
            mat[r][c]= "0"
            markIt_dfs(mat, r, c+1) # right
            markIt_dfs(mat, r+1, c) # down
            markIt_dfs(mat, r-1, c) # up
            markIt_dfs(mat, r, c-1) # left
            return 
        
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    markIt_dfs(grid, r, c)
        return count
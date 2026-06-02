class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def markIt_dfs(mat, r, c):
            if r < 0 or r == len(mat) or c < 0 or c == len(mat[0]) or mat[r][c] == "0":
                return 
            mat[r][c]= "0"
            markIt_dfs(mat, r, c+1) # right
            markIt_dfs(mat, r+1, c) # down
            markIt_dfs(mat, r-1, c) # up
            markIt_dfs(mat, r, c-1) # left
            return 1
        
        R = len(grid)-1; C = len(grid[0])-1; count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                visited = markIt_dfs(grid, r, c)
                if visited == 1:
                    count += 1

        return count
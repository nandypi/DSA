class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid); COLUMNS = len(grid[0])

        def markIt_dfs(mat, r, c):
            if (r == 0 or c == 0 or r == ROWS-1 or c == COLUMNS-1) and mat[r][c] == 0:
                return False

            if mat[r][c] == 1:
                return True

            mat[r][c]= 1

            R = markIt_dfs(mat, r, c+1)
            D = markIt_dfs(mat, r+1, c)
            U = markIt_dfs(mat, r-1, c)
            L = markIt_dfs(mat, r, c-1)

            return False not in (R, D, U, L)
        
        count = 0
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 0:
                    if markIt_dfs(grid, r, c):
                        count += 1
        return count
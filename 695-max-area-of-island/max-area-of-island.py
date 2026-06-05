class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid); COLUMNS = len(grid[0])
        
        def dfs_area(mat, r, c, area = 0):
            if r < 0 or r >= ROWS or c < 0 or c >= COLUMNS or mat[r][c] == 0:
                return area
            
            mat[r][c] = 0
            area += 1

            area = dfs_area(mat, r+1, c, area)
            area = dfs_area(mat, r-1, c, area)
            area = dfs_area(mat, r, c+1, area)
            area = dfs_area(mat, r, c-1, area)

            return area

        max_area = 0
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 1:
                    area = dfs_area(grid, r, c)
                    if area > max_area:
                        max_area = area
        
        return max_area


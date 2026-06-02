class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            # Stepped outside -> island is open
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False

            # Water (or already visited) does not create a leak
            if grid[r][c] == 1:
                return True

            # Mark visited
            grid[r][c] = 1

            right = dfs(r, c + 1)
            down  = dfs(r + 1, c)
            up    = dfs(r - 1, c)
            left  = dfs(r, c - 1)

            return right and down and up and left

        count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    if dfs(r, c):
                        count += 1

        return count
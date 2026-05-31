class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def dfs(mat, r, c, oc, uc):

            if r >= len(mat) or c >= len(mat[0]) or r < 0 or c < 0 or mat[r][c] != oc or mat[r][c] == uc:
                return mat
            
            mat[r][c] = uc

            mat = dfs(mat, r-1, c, oc, uc) # up
            mat = dfs(mat, r, c+1, oc, uc) # right
            mat = dfs(mat, r, c-1, oc, uc) # left
            mat = dfs(mat, r+1, c, oc, uc) # down
            
            return mat
        
        mat = dfs(image, sr, sc, image[sr][sc], color)

        return mat
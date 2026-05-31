class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def dfs(mat, r, c, oc, uc, v):

            print(r, c, oc, uc)

            if r >= len(mat) or c >= len(mat[0]) or r < 0 or c < 0 or mat[r][c] != oc or (r,c) in v:
                return mat
            
            mat[r][c] = uc
            v.add((r,c))

            mat = dfs(mat, r-1, c, oc, uc, v) # up
            mat = dfs(mat, r, c+1, oc, uc, v) # right
            mat = dfs(mat, r, c-1, oc, uc, v) # left
            mat = dfs(mat, r+1, c, oc, uc, v) # down
            
            return mat
        
        visited = set()
        mat = dfs(image, sr, sc, image[sr][sc], color, visited)

        return mat
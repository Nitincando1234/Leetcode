class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        cache = {}      # (r, c) -> maxLength of ones
        def helper(r, c):
            if r >= ROW or c >= COL: return 0
            if (r, c) not in cache:
                right = helper(r, c + 1)
                bottom = helper(r + 1, c)
                diag = helper(r + 1, c + 1)
                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(right, bottom, diag)
                    
            return cache[(r, c)]
        
        helper(0, 0)
        return max(cache.values()) ** 2
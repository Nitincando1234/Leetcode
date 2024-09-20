class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowZero = False
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        
        for r in range(ROWS):
            for c in range(COLUMNS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0: matrix[r][0] = 0
                    else: rowZero = True
        
        for r in  range(1, ROWS):
            for c in range(1, COLUMNS):
                if matrix[0][c] == 0 or matrix[r][0] == 0: matrix[r][c] = 0
        
        if matrix[0][0] == 0: 
            for r in range(ROWS): matrix[r][0] = 0
        
        if rowZero: 
            for c in range(COLUMNS): matrix[0][c] = 0
                    
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        output = [[0] * n for _ in range(n)]
        start_row, start_col, end_row, end_col = 0, 0, n, n
        i = 0
        while start_row < end_row or start_col < end_col:
            # right
            for c in range(start_col, end_col):
                i += 1
                output[start_row][c] = i
            start_row += 1
            # down
            for r in range(start_row, end_row):
                i += 1
                output[r][end_col - 1] = i
            end_col -= 1
            # left
            for c in range(end_col - 1, start_col - 1, -1):
                i += 1
                output[end_row - 1][c] = i
            end_row -= 1
            # up
            for r in range(end_row - 1, start_row - 1, -1):
                i += 1
                output[r][start_col] = i
            start_col += 1
            
        return output
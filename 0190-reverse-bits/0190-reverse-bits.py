class Solution:
    def reverseBits(self, n: int) -> int:
        res, temp = 0, 0
        for i in range(32):
            lsb = n & 1
            temp = lsb << (31 - i)
            res = res | temp
            n = n >> 1
        return res
    
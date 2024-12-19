class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            prefix = set()
            for num in nums:
                prefix.add(num & mask)
            proposed_max = max_xor | (1 << i)
            for pre in prefix:
                if (pre ^ proposed_max) in prefix:
                    max_xor = proposed_max
        return max_xor
            
            
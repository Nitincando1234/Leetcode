class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        N = len(citations)
        l, r = 0, N - 1
        while l < r:
            mid = (l + r) // 2
            if citations[mid] >= N - mid: r = mid
            else: l = mid + 1
        
        if citations[l] == 0: return 0
        return N - l
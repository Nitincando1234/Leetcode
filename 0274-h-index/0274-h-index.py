class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paper_counts = [0] * (n + 1)
        
        for c in citations:
            paper_counts[min(n, c)] += 1
        
        h = n   # Citations
        paper = paper_counts[n]
        while paper < h:
            h -= 1
            paper += paper_counts[h]
        
        return h
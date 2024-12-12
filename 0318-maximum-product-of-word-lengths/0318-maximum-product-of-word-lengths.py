class Solution:
    def maxProduct(self, words: List[str]) -> int:
        lookup = defaultdict(set)
        for w in words:
            lookup[w] = set(w)
        def dont_share(i, j):
            if lookup[i] & lookup[j]: return False
            return True
        maximum = 0
        for i in words: 
            for j in words:
                if dont_share(i, j):
                    maximum = max(maximum, len(i) * len(j))
        return maximum
            
class Solution:
    @lru_cache
    def longestSubstring(self, s: str, k: int) -> int:
        maxLen = 0
        valid = True
        start, end = 0, 0
        freq = [0 for i in range(26)] 
        for char in s:
            freq[ord(char) - ord("a")] += 1
        
        for end in range(len(s)):
            if(0 < (freq[ord(s[end]) - ord("a")]) < k):
                maxLen = max(maxLen, self.longestSubstring(s[start: end], k))
                start = end + 1
                valid = False
        
        if valid:
            return len(s)
        else:
            return max(maxLen, self.longestSubstring(s[start: ], k))
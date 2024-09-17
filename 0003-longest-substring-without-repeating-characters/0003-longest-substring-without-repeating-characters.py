class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, l = 0, 0
        characterSet = set()
        
        for r in range(len(s)):
            while s[r] in characterSet:
                characterSet.remove(s[l])
                l += 1
            characterSet.add(s[r])
            res = max(r - l + 1, res)
            
        return res
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length, i = 0, len(s) - 1
        
        while s[i] == " ": i -= 1
        while s[i] != " " and i >= 0:
            length += 1
            i -= 1
        return length
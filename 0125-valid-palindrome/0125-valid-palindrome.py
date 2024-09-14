class Solution:
    def alnum_condition(self, s: str):
        if (("A" <= s <= "Z") or ("a" <= s <= "z") or ("0" <= s <= "9")): return True
        return False
    
    def lower(self, s: str):
        if "A" <= s <= "Z":
            return chr(ord(s) + 32)       # ord return the ASCII value of str
        return s
    
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        test = 0
        while left <= right:
            if not self.alnum_condition(s[left]):
                left += 1
                continue
            elif not self.alnum_condition(s[right]):
                right -= 1
                continue
            
            if self.lower(s[left]) != self.lower(s[right]): return False
            
            left += 1
            right -= 1
        
        return True
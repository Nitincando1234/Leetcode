class Solution:
    def isNumber(self, s: str) -> bool:
        digit, dec, exp, symbol = False, False, False, False
        for c in s:
            if c in "0123456789":
                digit = True
            elif c in "+-":
                if symbol or digit or dec: return False
                else: symbol = True
            elif c in "Ee":
                if not digit or exp: return False
                exp = True
                dec = False
                symbol = False
                digit = False
            elif c == ".":
                if dec or exp: return False
                else: dec = True
            else: return False
        return digit
                
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        mx = 0
        l, r = 0, 0
        for p in s:
            if p == "(": l += 1
            else: r += 1
            if l == r: mx = max(mx, r * 2)
            elif r > l: l, r = 0, 0
        l, r = 0, 0
        for p in reversed(s):
            if p == ")": r += 1
            else: l += 1
            if l == r: mx = max(mx, r * 2)
            elif l > r: l, r = 0, 0
        return mx
class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumOfDigits(n)
            if n == 1: return True
        return False
    def sumOfDigits(self, num):
        output = 0
        while num:
            rem = num % 10
            output += rem ** 2
            num = num // 10
        return output
    
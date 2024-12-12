class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3: return False
        def helper(first, second, remaining):
            if len(remaining) < max(len(first), len(second)): return False
            if (first[0] == "0" and len(first) != 1) or (second[0] == "0" and len(second) != 1): return False
            first = int(first)
            second = int(second)
            res = str(first + second)
            len_res = len(res)
            if len_res > len(remaining): return False
            if res == remaining[0: len_res]:
                if len_res == len(remaining): return True
                first = second
                second = res
                remaining = remaining[len_res: ]
                return helper(str(first), str(second), str(remaining))
            
            return False
        
        index1 = 0
        for index2 in range(index1 + 1, len(num)):
            for index3 in range(index2 + 1, len(num)):
                first = num[index1: index2]
                second = num[index2: index3]
                remaining = num[index3: ]
                if helper(first, second, remaining): return True
        return False
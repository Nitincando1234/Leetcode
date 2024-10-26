class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {"2": "abc",
                       "3": "def", 
                       "4": "ghi", 
                       "5": "jkl", 
                       "6": "mno", 
                       "7": "pqrs", 
                       "8": "tuv", 
                       "9": "wxyz"
                        }
        res = []
        def backtrack(i, currentComb):
            if len(currentComb) == len(digits): 
                res.append(currentComb)
                return
            for c in digitToChar[digits[i]]: backtrack(i + 1, currentComb + c)
        if digits: backtrack(0, "")
        return res
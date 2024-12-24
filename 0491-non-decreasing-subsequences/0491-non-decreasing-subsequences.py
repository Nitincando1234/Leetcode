class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start_idx, prev_num, temp_subs):
            if start_idx == len(nums):
                if len(temp_subs) > 1:
                    subseqs.append(temp_subs[:])
                return
            if nums[start_idx] >= prev_num:
                temp_subs.append(nums[start_idx])
                backtrack(start_idx + 1, nums[start_idx], temp_subs)
                temp_subs.pop()
            if nums[start_idx] != prev_num: backtrack(start_idx + 1, prev_num, temp_subs)
        subseqs = []
        backtrack(0, float("-inf"), [])
        return subseqs
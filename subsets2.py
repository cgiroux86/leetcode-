from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        def backtrack(nums, arr, stop):
            if stop == len(arr):
                if arr not in res:
                    res.append(arr)
                return

            for i in range(len(nums)):

                backtrack(nums[i + 1:], arr + [nums[i]], stop)

        for i in range(len(nums) + 1):

            backtrack(nums, [], i)
        return res

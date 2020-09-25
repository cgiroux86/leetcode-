class Solution:
    def minDifference(self, nums):
        # [5,3,2,4]

        d = set()

        for n in nums:
            d.add(n)

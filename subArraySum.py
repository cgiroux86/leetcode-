class Solution:
    def subarraySum(self, nums, k):
        seen = {0: 1}
        total = 0
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            diff = curr_sum - k
            if diff in seen:
                total += seen[diff]
                seen[diff] += 1
            if curr_sum in seen:
                seen[curr_sum] += 1
            else:
                seen[curr_sum] = 1
        print(total)
        return total


import collections


# class Solution(object):
#     def subarraySum(self, nums, k):
#         d = collections.defaultdict(int)
#         d[0] = 1  # for first subarray k-0=k
#         tmp_sum = 0
#         res = 0
#         for i in range(len(nums)):
#             tmp_sum += nums[i]
#             if tmp_sum - k in d:
#                 res += d[tmp_sum - k]
#             d[tmp_sum] += 1
#         return res


s = Solution()
s.subarraySum([1, 2, 1, 2, 1], 3)

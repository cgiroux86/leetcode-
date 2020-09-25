class Solution:
    def checkSubarraySum(self, nums, k):
        sumi = 0
        dictionary = {0: -1}
        # O(N)
        if k == 0:
            for i in range(1, len(nums)):
                if nums[i] == 0 and nums[i - 1] == 0:
                    return True
            return False
        for i in range(len(nums)):
            sumi = (sumi + nums[i]) % k
            if sumi in dictionary:
                j = dictionary[sumi]
                if i - j >= 2:
                    return True
            else:
                dictionary[sumi] = i
        return False
# class Solution:
#     def checkSubarraySum(self, nums, k):
#         start = 0
#         end = 0
#         total = 0

#         while start < len(nums) and end < len(nums):
#             if end == len(nums) - 1:
#                 end -= 1
#                 total -= nums[end]
#             total += nums[end]
#             if start == end:
#                 return False
#             try:
#                 if total % k == 0 and end - start > 0:
#                     return True
#             except ZeroDivisionError:
#                 if total == 0 and end - start > 0:
#                     return True
#                 else:
#                     end += 1
#             if total < k:
#                 end += 1
#             if total > k:
#                 total -= nums[start]
#                 start += 1
#                 if end == 0:
#                     end += 1
#         return False


s = Solution()

print(s.checkSubarraySum([23, 2, 4, 6, 7], 17))

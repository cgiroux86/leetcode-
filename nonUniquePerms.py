class Solution:
    def permuteUnique(self, nums):
        combos = set()

        def permute(nums, combos):
            if len(nums) == 1:
                return [nums]
            permutations = []
            for i in range(len(nums)):
                perms = permute(nums[:i] + nums[i + 1:], combos)
                for p in perms:
                    permutations.append([nums[i], *p])
            if tuple(permutations) not in combos:
                return permutations
            else:
                return []

        return permute(nums, combos)


s = Solution()
s.permuteUnique([2, 2, 1, 1])

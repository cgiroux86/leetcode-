class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        if len(nums) == 1:
            return TreeNode(nums[0])
        curr_max = max(nums)
        pivot = nums.index(curr_max)
        root = TreeNode(curr_max)
        root.left = self.constructMaximumBinaryTree(nums[:pivot])
        root.right = self.constructMaximumBinaryTree(nums[pivot + 1:])
        return root

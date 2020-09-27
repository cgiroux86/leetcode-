# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root):
        if new_root == -1:
            new_root = root
        if new_root is None:
            return
        root.val = self.dft(root, new_root.val)
        self.bstToGst(root, new_root.left)
        self.bstToGst(root, new_root.right)
        return root

    def dft(self, root, target=None):
        print(target)
        if not root:
            return 0
        if root.val >= target:
            return root.val + self.dft(root.right, target) + self.dft(root.left, target)
        else:
            return 0 + self.dft(root.left, target) + self.dft(root.right, target)

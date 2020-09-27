# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0

    def bstToGst(self, root):
        if not root:
            return
        self.bstToGst(root.right)
        self.total += root.val
        root.val = self.total
        self.bstToGst(root.left)
        return root

        # def dft(root):
        #     nonlocal total
        #     if not root:
        #         return

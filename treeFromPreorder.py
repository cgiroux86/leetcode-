class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder):
        root = TreeNode(preorder[0])
        curr = root
        stack = [root]

        def insert(root, val):
            print(root, val)
            if not root:
                return
            if root.val > val:
                if not root.left:
                    root.left = TreeNode(val)
                else:
                    return insert(root.left, val)
            if root.val < val:
                if not root.right:
                    root.right = TreeNode(val)

                else:
                    return insert(root.right, val)

            return root
        for i in range(1, len(preorder)):
            insert(root, preorder[i])
        return root


s = Solution()
s.bstFromPreorder([8, 5, 1, 7, 10, 12])

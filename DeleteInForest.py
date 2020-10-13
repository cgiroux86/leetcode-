# // Given the root of a binary tree, each node in the tree has a distinct value.

# // After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

# // Return the roots of the trees in the remaining forest.  You may return the result in any order.

# // Example 1:

# // Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# // Output: [[1,2,null,4],[6],[7]]

class Solution:
    def delNodes(self, root, to_delete):
        results = []
        to_delete = set(to_delete)

        def dft(root, to_delete):
            if not root:
                return
            dft(root.left, to_delete)
            dft(root.right, to_delete)
            if root.left and root.left.val in to_delete:
                root.left = None
            if root.right and root.right.val in to_delete:
                root.right = None
            if root.val in to_delete:
                if root.right:
                    results.append(root.right)
                    root.right = None
                if root.left:
                    results.append(root.left)
                    root.left = None
        dft(root, to_delete)
        if root.val not in to_delete:
            results.append(root)
        return results

from binary_tree import TreeNode

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        ## recursive
        if root is None:
            return None

        invert = self.invertTree
        root.left, root.right = invert(root.right), invert(root.left)
            
        return root

        # ## iterative
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         node.left, node.right = node.right, node.left
        #         stack += node.left, node.right
        # return root

# >>> from binary_tree import Tree, TreeOps
# >>> from invert_binary_tree import Solution
# >>> root = Tree([4,2,7,1,3,6,9]).root
# >>> inverted_tree = Solution().invertTree(root)
# >>> TreeOps().printTree(inverted_tree)
# [4, 7, 2, 9, 6, 3, 1]
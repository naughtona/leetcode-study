from binary_tree import TreeNode

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

            
# >>> from maximum_depth_of_binary_tree import Solution
# >>> from binary_tree import Tree
# >>> root = Tree([3,9,20,None,None,15,7]).root
# >>> Solution().maxDepth(root)
# 3
# >>> root = Tree([1,None,2]).root
# >>> Solution().maxDepth(root)
# 2
# >>> root = Tree([]).root
# >>> Solution().maxDepth(root)
# 0
# >>> root = Tree([0]).root
# >>> Solution().maxDepth(root)
# 1
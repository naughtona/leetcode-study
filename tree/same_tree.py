from binary_tree import TreeNode

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
        else:
            return p is q


# >>> from same_tree import Solution
# >>> from binary_tree import Tree
# >>> p = Tree([1,2,3]).root
# >>> q = Tree([1,2,3]).root
# >>> Solution().isSameTree(p,q)
# True
# >>> p = Tree([1,2]).root
# >>> q = Tree([1,None,2]).root
# >>> Solution().isSameTree(p,q)
# False
# >>> p = Tree([1,2,1]).root
# >>> q = Tree([1,1,2]).root
# >>> Solution().isSameTree(p,q)
# False

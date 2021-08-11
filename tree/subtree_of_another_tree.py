from collections import deque
from binary_tree import TreeNode

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def same(s, t):
            if s and t:
                return s.val == t.val and same(s.left, t.left) and same(s.right, t.right)
            return s is t

        deq = deque([s])
        while deq:
            node = deq.popleft()
            if same(node, t):
                return True
            if node:
                deq += node.left, node.right
        
        return False

# >>> from subtree_of_another_tree import Solution
# >>> from binary_tree import Tree, TreeOps
# >>> s = Tree([3,4,5,1,2]).root
# >>> t = Tree([4,1,2]).root
# >>> Solution().isSubtree(s,t)
# True
# >>> s = Tree([3,4,5,1,2,None,None,None,None,0]).root
# >>> t = Tree([4,1,2]).root
# >>> Solution().isSubtree(s,t)
# False
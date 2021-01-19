from typing import List
from collections import deque
from binary_tree import TreeNode

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        deq = deque([(0, root)])

        while deq:
            depth, node = deq.popleft()
            
            if node:
                if depth == len(res):
                    res.append([node.val])
                else:
                    res[depth] += [node.val]
                
                deq += (depth+1,node.left), (depth+1,node.right)
        return res

# >>> from binary_tree_level_order_traversal import Solution
# >>> from binary_tree import Tree, TreeOps
# >>> root = Tree([3,9,20,None,None,15,7]).root
# >>> Solution().levelOrder(root)
# [[3], [9, 20], [15, 7]]
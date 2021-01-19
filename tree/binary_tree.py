from collections import deque

# Definition for a binary tree.
class Tree:
    def __init__(self, data=[]):
        self.data = data
        self.root = self.buildTree(data, 0)
        
    def buildTree(self, data, index):
        node = None
        if index < len(data):
            if data[index] is None:
                return
            node = TreeNode(data[index])
            node.left = self.buildTree(data, 2 * index + 1)
            node.right = self.buildTree(data, 2 * index + 2)
        return node
        
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return 'TreeNode({})'.format((self.val,self.left,self.right))

class TreeOps:
    def printTree(self, root):
        data = []
        deq = deque([root])
        while deq:
            node = deq.popleft()
            if node:
                data.append(node.val)
                deq += node.left, node.right
        return data
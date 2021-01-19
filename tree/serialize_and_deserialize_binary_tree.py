from collections import deque
from binary_tree import TreeNode

class Codec:
    ## bfs approach
    def serialize(self, root):
        res = []
        deq = deque([root])

        while deq:
            node = deq.popleft()
            res.append(node.val if node else "null")
            if node:
                deq += node.left, node.right
        return "[" + ",".join([str(e) for e in res]) + "]"
        

    def deserialize(self, data):
        data_ = data.strip("[]").split(",")

        if not data_ or data_[0] == "null":
            return None
        
        root = TreeNode(int(data_[0]))
        deq = deque([root])

        cur_pos = 1
        while deq:
            node = deq.popleft()
            lchild = data_[cur_pos]
            rchild = data_[cur_pos+1]

            if lchild != "null":
                node.left = TreeNode(lchild)
                deq.append(node.left)
            if rchild != "null":
                node.right = TreeNode(rchild)
                deq.append(node.right)
            
            cur_pos += 2

        return root
        
        

        # ## preorder traversal approach
        # def serialize(self, root: TreeNode) -> str:
        #     def preorder_encode(node):
        #         if node:
        #             vals.append(str(node.val))
        #             preorder_encode(node.left)
        #             preorder_encode(node.right)
        #         else:
        #             vals.append("#")
        #     vals = []
        #     preorder_encode(root)
        #     return " ".join(vals)

        # def deserialize(self, data: str) -> TreeNode:
        #     def preorder_decode():
        #         val = next(vals)
        #         if val == "#":
        #             return None
        #         node = TreeNode(val)
        #         node.left = preorder_decode()
        #         node.right = preorder_decode()
        #         return node
        #     vals = iter(data.split())
        #     root = preorder_decode()
        #     return root

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class ListOps:
    def print_list(self, head):
        data = []; curr = head
        while curr:
            data.append(curr.val)
            curr = curr.next
        return data
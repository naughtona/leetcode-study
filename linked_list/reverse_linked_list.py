from linked_list import ListNode, ListOps

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
        return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return
        
        node1 = result = ListNode()
        node2 = evenCursor = ListNode()
        
        oddFlag: bool = True
        while head is not None:
            if oddFlag:
                node1.next = ListNode(head.val)
                node1 = node1.next
                oddFlag = False
            else:
                node2.next = ListNode(head.val)
                node2 = node2.next
                oddFlag = True
                
            head = head.next
        
        node1.next = evenCursor.next
        
        return result.next
        
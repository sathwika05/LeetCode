# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None and l2:
            return l2
        if l2==None and l1:
            return l1
        if l1==None and l2==None:
            return
        head=l3=ListNode(0)
        while(l1 and l2):
            if(l1.val>l2.val):
                l3.val=l2.val
                l2=l2.next
            else:
                l3.val=l1.val
                l1=l1.next
            if l1 and l2:
                l3.next=ListNode(0)
                l3=l3.next
        if l1:
            l3.next=l1
        if l2:
            l3.next=l2
        return head
                        
                    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev=None
        l3=head
        while(head):
            if (head.val==val):
                if prev==None:
                    head=head.next
                    l3=l3.next
                else:
                    head=head.next
                    prev.next=head
            else:
                prev=head
                head=head.next
        return l3        

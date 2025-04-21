# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length=0
        temp=head
        while temp is not None:
            length+=1
            temp=temp.next
        
        pos=length-n
        temp=head

        if pos==0:
            return head.next

            
        for _ in range(pos-1):
            temp=temp.next
        
        if temp.next:
            temp.next=temp.next.next

        return head
        

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:

        temp=head
        deci=0
        sqr=0
        length=0

        while temp:
            length+=1
            temp=temp.next

        temp=head
        sqr=length-1

        while temp:
            if temp.val==1:
                deci+=2**sqr
            
            sqr-=1
            temp=temp.next

        
        return deci
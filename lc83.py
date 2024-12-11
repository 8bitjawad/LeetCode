# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        s=set()
        slow=head   

        if not head:
            return None

        s.add(slow.val)
        
        while slow and slow.next:
                
            if slow.next.val in s:
                slow.next=slow.next.next
            
            else:
                s.add(slow.next.val)
                slow=slow.next
            
        return head

        
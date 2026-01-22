# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sl = head
        fs = head
        while fs and fs.next:
            sl = sl.next
            fs = fs.next.next

            if sl == fs:
                return True
        return False
### https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        min_d = -1
        max_d = -1

        cur_d = -1
        priv = head.val

        while head.next:

            if (priv < head.val > head.next.val) or (priv > head.val < head.next.val):
                max_d = cur_d if min_d < 0 else max_d + cur_d
                min_d = cur_d if min_d < 0 else min(min_d, cur_d)
                cur_d = 0
            priv = head.val
            head = head.next

            if cur_d >= 0:
                cur_d += 1
        return [min_d, max_d]
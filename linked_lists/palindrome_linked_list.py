# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#Solução com tempo: O(n) e espaço: O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []

        while head is not None:
            arr.append(head.val)
            head = head.next

        return arr == arr[::-1]
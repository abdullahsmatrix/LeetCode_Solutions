# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry: int = 0 #this variable will carry second digit if sum > 9
        result = ListNode()
        current = result
        while l1 or l2 or carry:
            val1: int = l1.val if l1 else 0 #since list size varies it may not exist
            val2: int = l2.val if l2 else 0
            res = val1 + val2 + carry

            carry: int = res // 10 #carries first digit of res
            digit: int = res % 10 #second digit to append in the returning list

            current.next = ListNode(digit) #appending in current.val will leave 0 in the last node
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result.next


        

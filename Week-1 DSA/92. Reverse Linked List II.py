# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head.next or left == right:
            return head

        c = head
        counter = 0

        while c.next and counter < (left - 1):
            pre = c
            c = c.next
            counter += 1

        prev = None
        for _ in range((right - left) + 1):
            n = c.next
            c.next = prev
            prev = c
            c = n

        if left == 1 and c==None:
            head = prev
            return head
        if left==1 and c !=None:
            pre=head
            pre.next=c
            head=prev
            return head
            

            
        pre.next.next = c
        pre.next = prev

        return head

        
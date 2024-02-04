# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        curr = head

        while curr.next:
            if curr.val > curr.next.val:

                temp = curr.next
                prev = dummy
                while prev.next.val < temp.val:
                    prev = prev.next

    
                curr.next = temp.next
                temp.next = prev.next
                prev.next = temp
            else:
               
                curr = curr.next

        return dummy.next
        
        
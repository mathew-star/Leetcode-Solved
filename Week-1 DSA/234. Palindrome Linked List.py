# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head.next == None:
            return True
        if not head:
            return None
        check=None
        res=[]
        c=head
        while c:
            res.append(c.val)
            c=c.next
        c=head
        while c:
            i=res.pop()
            if i == c.val:
                check =True
                c=c.next
            else:
                return False

        return check

        
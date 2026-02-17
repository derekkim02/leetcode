# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        head1, head2 = (list1, list2) if list1.val <= list2.val else (list2, list1)

        start = head1

        while head1.next != None:
            head1_next = head1.next
            if head1_next.val >= head2.val:
                head1.next = head2
                head2 = head1_next
            head1 = head1.next
        
        head1.next = head2

        return start
    
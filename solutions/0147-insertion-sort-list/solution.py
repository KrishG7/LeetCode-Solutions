# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Anchor for our new, sorted list
        dummy = ListNode(0)

        # Pointer to iterate through the original, unsorted list
        curr = head

        while curr:
            # For every node, start searching from the beginning of the sorted list
            prev = dummy

            # Walk forward until we find a node greater than curr (or hit the end)
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # Save the next unsorted node so we don't lose the rest of the original list!
            next_node = curr.next

            # Insert curr perfectly between prev and prev.next
            curr.next = prev.next
            prev.next = curr

            # Shift our focus to the next unsorted node
            curr = next_node

        # Return the actual start of the sorted list (skipping the fake dummy)
        return dummy.next


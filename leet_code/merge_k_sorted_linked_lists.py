'''
Notes
* Use queue.PriorityQueue (put and get) for heap API
* Linked list trick - use a dummy head to make initialization logic cleaner, throw away before returning linked list (return head.next)
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from Queue import PriorityQueue
        head = current_node = ListNode(0)

        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            next_node = node.next
            current_node.next = ListNode(val)
            current_node = current_node.next
            if next_node:
                q.put((next_node.val, next_node))
        return head.next

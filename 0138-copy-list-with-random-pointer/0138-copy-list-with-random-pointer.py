"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        old_to_new_map = {}
        old_to_new_map[None] = None
        # first sweep to create all nodes
        cur = head
        while cur:
            old_to_new_map[cur] = Node(cur.val)
            '''            print(cur.val, cur.next, cur.random)
            print(
                old_to_new_map[cur].val,
                old_to_new_map[cur].next,
                old_to_new_map[cur].random,
            )'''
            cur = cur.next

        # second sweep to create next links and random links
        cur = head
        while cur:
            #print(cur)
            old_to_new_map[cur].next = old_to_new_map[cur.next]
            old_to_new_map[cur].random = old_to_new_map[cur.random]
            cur = cur.next

        return old_to_new_map[head]

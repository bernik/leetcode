from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"ListNode[{self.val}]"



class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        xs = []
        tmp = 0 
        while l1 or l2:
            v1 = 0
            v2 = 0 
            if l1:
                v1 = l1.val
                l1 = l1.next

            if l2:
                v2 = l2.val
                l2 = l2.next

            x = v1 + v2 + tmp
            if x >= 10:
                tmp = 1
                x = x % 10
            else:
                tmp = 0

            xs.append(x)

        if tmp > 0:
            xs.append(tmp)

        l = None
        for x in reversed(xs):
            l = ListNode(x, l)

        return l



def print_list(l: Optional[ListNode]):
    res = []
    while l:
        res.append(l.val)
        l = l.next

    print(res)


def to_list_nodes(arr: List[int]) -> Optional[ListNode]:
    l = None
    for x in reversed(arr):
        l = ListNode(x, l)

    return l
# l1 = [2,4,3]
# l2 = [5,6,4]
# exp = [7,0,8]
s = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
print_list(s.addTwoNumbers(l1, l2))

# [9,9,9,9,9,9,9]
# [9,9,9,9]
# [8,9,9,9,0,0,0,1]
print_list(s.addTwoNumbers(to_list_nodes([9,9,9,9,9,9,9]), to_list_nodes([9,9,9,9])))
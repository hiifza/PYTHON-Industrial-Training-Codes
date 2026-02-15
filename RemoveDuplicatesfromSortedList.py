# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import *

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p:
            if p.next != None and p.val == p.next.val:
                temp = p.next
                p.next = temp.next
                temp.next = None
            else :
                p = p.next
        return head
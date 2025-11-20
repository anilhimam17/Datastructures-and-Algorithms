#This is an algorithm that accepts two sorted linked lists and merges them into a single sorted linked list.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def reverseList(self, list1, list2):
        dummy = ListNode(0)
        current = dummy

        # Append list1 to the new list
        while list1 and list2:
            if list1.value > list2.value:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next

            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2
        return dummy.next
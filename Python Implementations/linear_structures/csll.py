from typing import Any


# Will add generics after the complete impl.
class Node:
    """Class that implements the Nodes that compose the elements of the CSLL."""
    # ==== Legacy ====
    def __init__(self, value: Any):
        self.value = value
        self.next: Node | None = None

    def __str__(self):
        return f"Node(value={self.value}, next={self.next})"

class CSLL:
    """Class that implements all the behaviour of the Circular Singly-Linked List."""
    # ==== Legacy ====
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.no_of_elements: int = 0

    def __str__(self):
        """Provides a string repr of the list of nodes."""
        list_str = ""
        # If the list is empty
        if not self.head:
            list_str += "None <= Head\nNone <= Tail\n"
        # If there is only one element in the list
        elif self.no_of_elements == 1:
            list_str += f"{self.head} <= Head\n{self.tail} <= Tail\n"
        # If the list is not empty
        else:
            cursor = self._head
            while cursor:
                if cursor == self.head:
                    list_str += f"{cursor.value} <= Head\n"
                elif cursor == self.tail:
                    list_str += f"{cursor.value} <= Tail\n"
                    break
                else:
                    list_str += f"{cursor.value}\n"
                # Updating the loop control variable for traversal
                cursor = cursor.next

        return list_str

    # ==== Helper Properties to update the pointers ====
    @property
    def _head(self):
        assert self.head is not None, "The head is currently none."
        return self.head
    
    @property
    def _tail(self):
        assert self.tail is not None, "The tail is currently none."
        return self.tail
    
    # ==== Properties of the CSLL ====
    def append(self, value: int):
        """Adds a new node to the end of the list."""
        new_node: Node = Node(value)
        
        # If the list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        # If the list is not empty
        else:
            tail = self._tail
            tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

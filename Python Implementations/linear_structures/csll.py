from typing import Any


# Will add generics after the complete impl.
class Node:
    """Class that implements the Nodes that compose the elements of the CSLL."""
    # ==== Legacy ====
    def __init__(self, value: Any):
        self.value = value
        self.next: Node | None = None

    def __str__(self):
        return f"Node(value={self.value})"

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
    
    def __iter__(self):
        """Provides an iterator for the CSLL."""
        if not self._head:
            raise IndexError("The list is current empty.")
        else:
            cursor: Node = self._head
            while cursor:
                yield cursor

                # Exit Condition
                if cursor == self._tail:
                    break

                # Update the loop control variable
                assert cursor.next is not None, "Cursor cannot be none during traversal."
                cursor = cursor.next

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

        # Updating the no of elements
        self.no_of_elements += 1

    def insert(self, value: int, index: int):
        """Inserts the value at a given index in the list."""
        if index < 0 or index >= self.no_of_elements:
            raise IndexError("The requested index is out of bounds.")
        else:
            # Adds the node at the start of the list.
            new_node: Node = Node(value)
            if index == 0:
                new_node.next = self._head
                self.head = new_node
                self._tail.next = self.head
            # Adds the element at the end of the list.
            elif index == self.no_of_elements - 1:
                self.append(value)
                return
            # Adds the element at any random index of the list.
            else:
                cursor = self._head
                # Traversing to the idx - 1 to add the new node.
                for _ in range(index - 1):
                    assert cursor.next is not None, "Cursor cannot be None during traversal."
                    cursor = cursor.next
                
                # Updating the links
                assert cursor.next is not None, "The next ptr cannot be None in the middle of the list."
                new_node.next = cursor.next
                cursor.next = new_node

            # Updating the no of elements
            self.no_of_elements += 1

    def search(self, value: int):
        """Returns a integer after searching for a given value in the list."""
        for idx, node in enumerate(self):
            if node.value == value:
                return idx
        return -1
    
    def get(self, index: int):
        """Returns the node at a given index of the list."""
        if index < 0 or index >= self.no_of_elements:
            raise IndexError("The requested index is out of bounds for the given list.")
        else:
            for idx, node in enumerate(self):
                if idx == index:
                    return node
    
    def set(self, value: int, index: int):
        """Updates the value of given index of the list."""
        if index < 0 or index >= self.no_of_elements:
            raise IndexError("The requested index is out of bounds for the given list.")
        else:
            update_node = self.get(index)
            assert update_node is not None, "The get function cannot return a None."
            update_node.value = value
    
    def pop():
        raise NotImplementedError
    
    def remove():
        raise NotImplementedError
    
    def clear():
        raise NotImplementedError

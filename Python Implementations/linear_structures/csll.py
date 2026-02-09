from typing import Any, Generator


# Will add generics after the complete impl.
class Node:
    """Class that implements the Nodes that compose the elements of the CSLL."""
    # ==== Standard Methods ====
    def __init__(self, value: Any):
        self.value = value
        self.next: Node | None = None

    def __str__(self):
        return f"Node(value={self.value})"


class CSLL:
    """Class that implements all the behaviour of the Circular Singly-Linked List."""
    
    # ==== Standard Methods ====
    def __init__(self) -> None:
        
        self.head: Node | None = None
        self.tail: Node | None = None
        self.no_of_elements: int = 0

    def __str__(self) -> str:
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
    
    def __iter__(self) -> Generator[Node, Any, Any]:
        """Provides an iterator for the CSLL."""
        
        if not self._head:
            raise IndexError("The list is current empty.")
        else:
            cursor: Node = self._head
            while cursor:
                yield cursor

                # Exit Condition for Infinite Loop
                if cursor == self._tail:
                    break

                # Update the loop control variable
                assert cursor.next is not None, "Cursor cannot be none during traversal."
                cursor = cursor.next

    # ==== Helper Properties to update the pointers ====
    @property
    def _head(self) -> Node:
        
        assert self.head is not None, "The head is currently none."
        return self.head
    
    @property
    def _tail(self) -> Node:
        
        assert self.tail is not None, "The tail is currently none."
        return self.tail
    
    # ==== Properties of the CSLL ====
    def append(self, value: int) -> None:
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

    def insert(self, value: int, index: int) -> None:
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

    def search(self, value: int) -> int:
        """Returns a integer after searching for a given value in the list."""
        
        for idx, node in enumerate(self):
            if node.value == value:
                return idx
        return -1
    
    def get(self, index: int) -> Node | None:
        """Returns the node at a given index of the list."""
        
        if index < 0 or index >= self.no_of_elements:
            raise IndexError("The requested index is out of bounds for the given list.")
        else:
            for idx, node in enumerate(self):
                if idx == index:
                    return node
            else:
                return None
    
    def set(self, value: int, index: int) -> None:
        """Updates the value of given index of the list."""
        
        if index < 0 or index >= self.no_of_elements:
            raise IndexError("The requested index is out of bounds for the given list.")
        else:
            # Accessing the corresponding Node 
            update_node = self.get(index)

            # If no Node was found
            assert isinstance(update_node, Node), "No node found at given index."

            # Update Node
            update_node.value = value
    
    def pop(self) -> Node:
        """Removes the very last node from the list and returns it."""
        
        if not self.head:
            raise IndexError("The list is currently empty and has no elements that can be popped.")
        else:
            # If only one element is left in the list
            remove_node: Node | None = None
            if self.no_of_elements == 1:
                remove_node = self._head
                self.head = None
                self.tail = None
            else:
                remove_node = self._tail
                previous_node = self.get(self.no_of_elements - 2)
                assert previous_node is not None, "The previous node cannot be none in the middle of the list."
                previous_node.next = self._head
                remove_node.next = None
                self.tail = previous_node
        
            # Updating the no of elements in the list.
            self.no_of_elements -= 1
            return remove_node
    
    def remove(self, index: int) -> None:
        """Removes any node identified by its index in the list."""
        
        if index < 0 or index >= self.no_of_elements:
            raise IndexError("The requested index was out of bounds.")
        else:
            remove_node: Node | None = None
            if index == 0:
                remove_node = self._head
                self.head = self._head.next
                self._tail.next = self.head
                remove_node.next = None
            elif index == self.no_of_elements - 1:
                self.pop()
                return
            else:
                remove_node = self.get(index)
                assert remove_node is not None, "The remove node cannot be none within the bounds of the list."
                previous_node = self.get(index - 1)
                assert previous_node is not None, "The previous node cannot be none in the middle of the list."
                previous_node.next = remove_node.next
                remove_node.next = None

            # Updating the number of elements in the list
            self.no_of_elements -= 1
            del remove_node

            # Updating the pointers if the elements is 0
            if self.no_of_elements == 0:
                self.head = None
                self.tail = None
    
    def clear(self) -> None:
        """Clears all the nodes in the list."""
        
        self.head = None
        self.tail = None
        self.no_of_elements = 0

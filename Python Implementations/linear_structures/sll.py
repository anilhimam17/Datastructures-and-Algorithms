from typing import Any, cast


class Node:
    """Implements the node class for providing a container for other datastructures."""
    def __init__(self, value: Any, next_ptr = None) -> None:
        self.value: Any = value
        self.next: None | Node = next_ptr

    def __repr__(self) -> str:
        """Returns a programmer level repr of the node."""
        return f"Node(value={self.value}, next={self.next})"
    
    def __str__(self) -> str:
        """Returns a high level repr of the node."""
        return f"Value -> {self.value}"


class SLL:
    """Implements a class that illustrates the properties and functions of a Singly-Linked List."""
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.no_of_elements: int = 0

    # Help properties to check for the Noneness of the pointers in the SLL.
    @property
    def _head(self) -> Node:
        assert self.head is not None, "Head is currently none."
        return self.head
    
    @property
    def _tail(self) -> Node:
        assert self.tail is not None, "Tail is currently none."
        return self.tail

    def append(self, value: Any) -> None:
        """Adds nodes to the end of the SLL."""
        new_node = Node(value)

        # If the SLL is empty.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the SLL is not empty.
        else:
            self._tail.next = new_node
            self.tail = new_node

        # Update the no of elements in the SLL.
        self.no_of_elements += 1

    def insert(self, value: Any, position: int | None = None) -> None:
        """Inserts new nodes at any location in the SLL."""
        ll_index = 0 if position is None else position

        # Bounds Check
        if ll_index > self.no_of_elements or ll_index < 0:
            raise IndexError("Given element insertion position is out of bounds")
        
        new_node: Node = Node(value)
        # Inserting new node at the start of the SLL.
        if ll_index == 0:
            # Step - 1: Update the next_ptr of th new node to the current head.
            new_node.next = self.head
            # Step - 2: Update the head to the new node.
            self.head = new_node
            # Edge Case
            if self.no_of_elements == 0:
                self.tail = new_node
        # Inserting new node at the end of the SLL.
        elif ll_index == self.no_of_elements:
            self.append(value)
            return
        # Inserting new node at any index of the SLL.
        else:
            # Step - 1: Traversing to the n - 1th index
            cursor = self._head
            for _ in range(ll_index - 1):
                assert cursor is not None, "Cursor should not be none during traversal."
                cursor = cursor.next

            # Interim Step: Casting to Node after bounds check
            cursor = cast(Node, cursor)

            # Step - 2: Insertion of the element
            new_node.next = cursor.next
            cursor.next = new_node

        # Updating the no of elements
        self.no_of_elements += 1

    def search(self, value: Any) -> bool:
        """Searched for an element and returns the element or -1."""
        if self._head:
            cursor = self.head
            while cursor:
                if cursor.value == value:
                    return True
                cursor = cursor.next
            return False
        else:
            raise IndexError("The List is empty")
        
    def get(self, index: int) -> Node:
        """Returns the node at given index."""
        if index >= self.no_of_elements or index < 0:
            raise IndexError("The requested index is out of bounds.")
        else:
            cursor = self._head
            for _ in range(index):
                assert cursor is not None, "Cursor should not be none during traversal."
                cursor = cursor.next
            assert cursor is not None, "Cursor should not be none during traversal."
            return cursor
        
    def set(self, index: int, value: Any) -> bool:
        """Updates the value of a node at a given index."""
        if index >= self.no_of_elements or index < 0:
            raise IndexError("The requested index is out of bounds.")
        else:
            set_node = self.get(index)
            set_node.value = value
            return True
        
    def pop(self) -> Node:
        """Removes the last element and returns it by default."""
        # Bounds Check
        if self.no_of_elements == 0:
            raise IndexError("The list is empty and cannot be popped.")
        
        # If only one element is present in the SLL.
        if self.no_of_elements == 1:
            popped_node = self._head
            self.head = None
            self.tail = None
        # If there are more than one elements in the SLL.
        else:
            new_tail = self.get(self.no_of_elements - 2)
            popped_node = cast(Node, new_tail.next)
            self.tail = new_tail
            new_tail.next = None

        # Updating the no of elements
        self.no_of_elements -= 1
        return popped_node
        
    def remove(self, index: int) -> Node:
        """Removes the element at any index from the SLL."""
        if index >= self.no_of_elements or index < 0:
            raise IndexError("The index is out of bounds / or the list is empty.")
        
        # Node that is being removed
        remove_node: Node

        # If the first element is being removed.
        if index == 0:
            remove_node = self._head
            self.head = self._head.next
            assert remove_node is not None, "Node to be removed cannot be none."
            remove_node.next = None
        # If the element being removed is the last.
        elif index == self.no_of_elements - 1:
            return self.pop()
        else:
            # Traversing to search for the penultimate element
            prev_node = self.get(index - 1)
            assert prev_node.next, "The node before the remove node cannot be none."
            remove_node = prev_node.next
            assert remove_node is not None, "Node to be removed cannot be none."

            # Updating the links
            if remove_node.next is not None:
                prev_node.next = remove_node.next
            else:
                prev_node.next = None
            remove_node.next = None

        # Updating the no of elements
        self.no_of_elements -= 1

        # Returning the removed node.
        return remove_node

    def clear(self) -> None:
        """Removes all the elements from the SLL."""
        self.head = None
        self.tail = None
        self.no_of_elements = 0

    def __repr__(self) -> str:
        raise NotImplementedError
        
    def __str__(self) -> str:
        """Provides a string repr of the SLL."""
        if self.no_of_elements == 0:
            return f"Current Number of Element: {self.no_of_elements}\nNone <= Head\nNone <= Tail\n"
        elif self.no_of_elements == 1:
            return f"Current Number of Element: {self.no_of_elements}\n{self._head.value} <= Head\n{self._tail.value} <= Tail\n"
        else:
            cursor = self._head
            display_str = f"Current Number of Element: {self.no_of_elements}\n"
            while cursor:
                if cursor == self.head:
                    display_str += f"{cursor.value} <= Head\n"
                elif cursor == self.tail:
                    display_str += f"{cursor.value} <= Tail\n"
                else:
                    display_str += f"{cursor.value}\n"
                cursor = cursor.next

            return display_str
        
    def __iter__(self):
        """Iterator for the SLL object."""
        cursor = self._head
        while cursor:
            yield cursor
            cursor = cursor.next

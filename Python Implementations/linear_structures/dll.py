from typing import Any, Generator


class Node:
    """Class implements the new node structure required for Doubly Linked Lists."""
    # ==== Standard Functions ====
    def __init__(self, value: Any) -> None:
        self.prev: Node | None = None
        self.next: Node | None = None
        self.value: Any = value

    def __str__(self) -> str:
        """String Repr of each node."""
        return f"Node(value={self.value})"
    

class DLL:
    """Class implements a generalised Doubly Linked List."""
    # ==== Standard Functions ====
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.no_of_elements: int = 0

    def __str__(self) -> str:
        """String repr of the DLL."""
        str_repr: str = ""

        # If the list is empty
        if not self.head:
            str_repr = "None <- Head\nNone <- Tail\n"
        # If the list is not empty
        else:
            cursor: Node = self._head
            while cursor:
                if cursor == self._head:
                    str_repr += f"{cursor.value} <- Head\n"
                elif cursor == self._tail:
                    str_repr += f"{cursor.value} <- Tail\n"
                    break
                else:
                    str_repr += f"{cursor.value}\n"
                # Updating the loop control variable
                assert cursor.next is not None, "Cursor cannot be none during traversal."
                cursor = cursor.next
        # Returning the visual repr of the DLL
        return str_repr
    
    def __iter__(self) -> Generator[Any, Any, Any]:
        """Provides an iterator for the DLL."""
        if self.head is None:
            raise IndexError("The list doesn't contain any nodes for iteration.")
        else:
            cursor: Node = self.head
            while cursor:
                yield cursor

                # Loop Exit Condition
                if cursor == self.tail:
                    break

                # Updating the loop variable
                assert cursor.next is not None, "Cursor cannot be none during __iter__."
                cursor = cursor.next
                    
        
    # ==== Helper Properties ====
    @property
    def _head(self) -> Node:
        assert self.head is not None, "The head is currently None."
        return self.head
    
    @property
    def _tail(self) -> Node:
        assert self.tail is not None, "The tail is currently None."
        return self.tail
    
    # ==== Properties of the DLL ====
    def append(self, value: int) -> None:
        """Adds a new node to the end of the list."""
        new_node: Node = Node(value)

        # If the list is empty.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty.
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self.tail = new_node
        
        # Updating the number of elements
        self.no_of_elements += 1

    def insert(self, value: int, index: int) -> None:
        """Adds a node to the given index in the list."""
        if index < 0 or index > self.no_of_elements:
            raise IndexError("The entered index for insertion is out of bounds.")
        else:
            new_node: Node = Node(value)
            if index == 0:
                self._head.prev = new_node
                new_node.next = self._head
                self.head = new_node
            elif index == self.no_of_elements:
                self.append(value)
                return
            else:
                mid = int(self.no_of_elements / 2)
                cursor: Node
                if index < mid:
                    cursor = self._head
                    for i in range(mid - 1):
                        if i == index:
                            break
                        assert cursor.next is not None, "Cursor cannot be none during traversal for insertion."
                        cursor = cursor.next
                else:
                    cursor = self._tail 
                    for i in range(self.no_of_elements - 1, mid - 1, -1):
                        if i == index:
                            break
                        assert cursor.prev is not None, "Cursor cannot be none during traversal for insertion."
                        cursor = cursor.prev
                
                # Updating the links
                new_node.prev = cursor.prev
                assert cursor.prev is not None, "The previous node cannot be none in the middle of the list."
                cursor.prev.next = new_node
                new_node.next = cursor
                cursor.prev = new_node
            
            # Updating the no of elements
            self.no_of_elements += 1

    def search(self, value: int) -> int:
        """Searches for a value and returns an index of the first occurrence or -1."""
        for idx, node in enumerate(self):
            if node.value == value:
                return idx
        return -1
    
    def get(self, index: int) -> Node:
        """Returns the node at a given index."""
        if index < 0 or index >= self.no_of_elements:
            raise IndexError("The requested index is out of bounds.")
        else:
            if index == 0:
                return self._head
            elif index == self.no_of_elements - 1:
                return self._tail
            else:
                mid = int(self.no_of_elements / 2)
                cursor: Node
                if index < mid:
                    cursor = self._head
                    for i in range(mid - 1):
                        assert cursor.next is not None, "Cursor cannot be none during traversal for insertion."
                        cursor = cursor.next
                        if i == index:
                            break
                else:
                    cursor = self._tail 
                    for i in range(self.no_of_elements - 1, mid - 1, -1):
                        assert cursor.prev is not None, "Cursor cannot be none during traversal for insertion."
                        cursor = cursor.prev
                        if i == index:
                            break
                return cursor
            
    def set(self, value: int, index: int) -> None:
        """Updates the value of a given node identified by its index."""
        if index < 0 or index >= self.no_of_elements:
            raise IndexError("The requested index is out of bounds.")
        else:
            get_node: Node = self.get(index)
            get_node.value = value

    def pop(self) -> Node:
        """Removes the very last element in the list."""
        if self.head is None:
            raise IndexError("There are no elements remaining in the list that can be popped.")
        else:
            remove_node: Node
            if self.no_of_elements == 1:
                remove_node = self.head
                self.head = None
                self.tail = None
            else:
                remove_node = self._tail
                self.tail = self._tail.prev
                remove_node.prev = None
                assert self.tail is not None, "The second last element in the list cannot be none."
                self.tail.next = None
            
            # Updating the no of elements in the list.
            self.no_of_elements -= 1
            return remove_node

    def remove(self, index: int):
        """Removes the node at the specified index from the list."""
        if index < 0 or index >= self.no_of_elements:
            raise IndexError("The requested index is out of bounds.")
        else:
            remove_node: Node
            if index == 0:
                remove_node = self._head
                self.head = self._head.next
                remove_node.next = None
                assert self.head is not None, "The second element in the list cannot be none."
                self.head.prev = None
            elif index == self.no_of_elements - 1:
                self.pop()
                return
            else:
                # Accessing the element to be removed
                remove_node = self.get(index)
                
                # Updating the links of the surrounding elements
                assert remove_node.prev is not None, "A node in the middle of the list cannot be none."
                remove_node.prev.next = remove_node.next
                assert remove_node.next is not None, "A node in the middle of the list cannot be none."
                remove_node.next.prev = remove_node.prev

                # Updating the links of the remove element
                remove_node.next = None
                remove_node.prev = None

            # Updating the no of elements in the list
            self.no_of_elements -= 1

    def clear(self):
        """Clears all the elements in the list."""
        self.head = None
        self.tail = None
        self.no_of_elements = 0

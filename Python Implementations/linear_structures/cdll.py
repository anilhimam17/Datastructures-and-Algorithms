from typing import Any, Generator


class Node:
    """Implements the Node datastructure for the CDLL with Bi-Directional pointers."""
    # ==== Standard Methods ====
    def __init__(self, value: Any) -> None:
        self.value = value
        self.prev: Node | None = None
        self.next: Node | None = None

    def __str__(self) -> str:
        """Provides a string repr of the nodes."""
        return f"Node(value={self.value})"
    

class CDLL:
    """Implements the Circular Doubly Linked List datastructure."""
    # ==== Standard Methods ====
    def __init__(self) -> None:
        self.no_of_elements: int = 0
        self.head: Node | None = None
        self.tail: Node | None = None
    
    def __str__(self) -> str:
        """Provides a str repr of the CDLL."""
        repr_str: str = ""

        # If the list is empty
        if not self.head:
            repr_str = "None <= Head\nNone <= Tail\n"
        # If the list is not empty
        else:
            cursor: Node = self.head
            while True:
                # If the list has only one element
                if cursor == self.head and cursor == self.tail:
                    repr_str += f"{cursor.value} <= Head\n{cursor.value} <= Tail\n"
                    break
                elif cursor == self.head:
                    repr_str += f"{cursor.value} <= Head\n"
                elif cursor == self.tail:
                    repr_str += f"{cursor.value} <= Tail\n"
                    break
                else:
                    repr_str += f"{cursor.value}\n"
                
                # Updating the loop control variable
                assert cursor.next, "Cursors next node cannot be none in a multi-node list."
                cursor = cursor.next
        
        return repr_str
    
    def __iter__(self) -> Generator[Any, None, None]:
        """Returns an iterator to the CDLL."""
        if not self.head:
                raise IndexError("List doesn't contain any elements.")
        else:
            cursor: Node = self._head
            while True:
                yield cursor
                
                # Loop exit variable
                if cursor == self.tail:
                    break
                
                # Loop control variable
                assert cursor.next, "Cursor cannot be none in the middle of the list."
                cursor = cursor.next

    # ==== Helper Properties ====
    @property
    def _head(self) -> Node:
        assert self.head, "The head is currently none"
        return self.head

    @property
    def _tail(self) -> Node:
        assert self.tail, "The tail is currently none"
        return self.tail

    # ==== Properties of the CDLL ====
    def append(self, value: Any) -> None:
        """Adds a new node to the end of the list."""
        new_node: Node = Node(value)

        # If the list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.prev = new_node
            new_node.next = new_node
        # If the list is not empty
        else:
            new_node.next = self._tail.next
            new_node.prev = self.tail
            self._tail.next = new_node
            self.tail = new_node
            self._head.prev = new_node
        
        # Updating the no of elements in the list.
        self.no_of_elements += 1

    def insert(self, value: Any, index: int) -> None:
        """Adds a new node to a given index in the list."""
        new_node: Node = Node(value)

        # Bounds Check
        if index < 0 or index > self.no_of_elements:
            raise IndexError("The requested index is out of bounds.")
        else:
            # Inserting node at the start of the list.
            if index == 0:
                new_node.next = self._head
                new_node.prev = self._head.prev
                self._head.prev = new_node
                self.head = new_node
            # Inserting node at the end of the list.
            elif index == self.no_of_elements:
                self.append(value)
                return
            # Inserting the node at any random location.
            else:
                # Traversing to the adjacent node for insertion.
                cursor: Node
                mid: int = int(self.no_of_elements / 2)
                if index < mid:
                    cursor = self._head
                    for i in range(mid - 1):
                        if i == index:
                            break
                        assert cursor.next, "Cursor's next cannot be none in the middle of the list."
                        cursor = cursor.next
                else:
                    cursor = self._tail
                    for i in range(self.no_of_elements - 1, mid - 1, -1):
                        if i == index:
                            break
                        assert cursor.prev, "Cursor's prev cannot be none in the middle of the list."
                        cursor = cursor.prev
                
                # Updating the links
                new_node.next = cursor
                new_node.prev = cursor.prev
                assert cursor.prev, "The previous node cannot be none in the middle of the list."
                cursor.prev.next = new_node
                cursor.prev = new_node

            # Updating the no of elements in the list.
            self.no_of_elements += 1        

    def search(self, value: Any) -> int:
        """Returns the index of the first occurrence of a value in the list else -1."""
        for idx, node in enumerate(self):
            if node.value == value:
                return idx
        return -1
    
    def get(self, index: int) -> Node:
        """Returns the node identified by its index."""
        # Bounds Check
        if index < 0 or index >= self.no_of_elements:
            raise IndexError("The requested index is out of bounds.")
        else:
            # Inserting node at the start of the list.
            if index == 0:
                return self._head
            # Inserting node at the end of the list.
            elif index == self.no_of_elements - 1:
                return self._tail
            # Inserting the node at any random location.
            else:
                # Traversing to the adjacent node for insertion.
                cursor: Node
                mid: int = int(self.no_of_elements / 2)
                if index < mid:
                    cursor = self._head
                    for i in range(mid - 1):
                        if i == index:
                            break
                        assert cursor.next, "Cursor's next cannot be none in the middle of the list."
                        cursor = cursor.next
                else:
                    cursor = self._tail
                    for i in range(self.no_of_elements - 1, mid - 1, -1):
                        if i == index:
                            break
                        assert cursor.prev, "Cursor's prev cannot be none in the middle of the list."
                        cursor = cursor.prev
                
                return cursor
            
    def set(self, value: Any, index: int) -> None:
        """Updates the value of given node identified by its index."""
        if index < 0 or index >= self.no_of_elements:
            raise IndexError("The requested index is out of bounds.")
        else:
            get_node: Node = self.get(index)
            get_node.value = value

    def pop(self) -> Node:
        """Removes the last node of the list and returns it."""
        if not self.head:
            raise IndexError("The list currently doesn't have any elements that can be popped.")
        else:
            remove_node: Node
            
            # If there is only one element in the list.
            if self.no_of_elements == 1:
                remove_node = self._head
                self.head = None
                self.tail = None
            # Removing the last element in the list.
            else:
                remove_node = self._tail
                previous_node = self._tail.prev
                assert previous_node, "The second last node of the list cannot be none."
                previous_node.next = self._head
                self.tail = previous_node

            # Updating the links of the remove_node.
            remove_node.next = None
            remove_node.prev = None

            # Updating the no of elements in the list.
            self.no_of_elements -= 1
            return remove_node
        
    def remove(self, index: int) -> None:
        """Removes a node at the given index."""
        if index < 0 or index >= self.no_of_elements:
            raise IndexError("The requested index is out of bounds.")
        else:
            remove_node: Node

            # If the node to be removed is the first.
            if index == 0:
                remove_node = self._head
                next_node = self._head.next
                assert next_node, "The second node of the list cannot be none."
                next_node.prev = self.tail
                self.head = next_node
            # If the node to be removed is the last.
            elif index == self.no_of_elements - 1:
                self.pop()
                return
            # If the node to be removed is anywhere in between.
            else:
                remove_node = self.get(index)

                # Adjacent Nodes
                previous_node = remove_node.prev
                assert previous_node, "The previous node cannot be none in the middle of the list."
                next_node = remove_node.next
                assert next_node, "The next node cannot be none in the middle of the list."

                # Updating the links
                previous_node.next = next_node
                next_node.prev = previous_node

            # Updating the links of the remove node
            remove_node.next = None
            remove_node.prev = None

            # Updating the no of elements in the list.
            self.no_of_elements -= 1

    def clear(self):
        """Clears all the elements in the list."""
        self.head = None
        self.tail = None
        self.no_of_elements = 0

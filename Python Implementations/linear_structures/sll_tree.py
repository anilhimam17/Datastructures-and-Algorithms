from typing import Any, Generator


class Node:
    """Implements a Node Structure to be used in the LL."""
    # ==== Standard Methods ====
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Node | None = None

    def __str__(self) -> str:
        """Provides a string repr for the Node class."""
        return f"Node(value={self.value})"


class TreeNode:
    """Implements the Node Structure specific to the family on Trees in LL style."""
    # ==== Standard Methods ====
    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child: TreeNode | None = None
        self.right_child: TreeNode | None = None

    def __str__(self) -> str:
        """Provides a string representation of the TreeNode."""
        return f"TreeNode(value={self.value})"
    

class TreeSLL:
    """Implements the Singly - Linked List using the TreeNodes Structure for elements."""
    # ==== Standard Methods ====
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.no_of_elements = 0

    def __iter__(self) -> Generator[Any, None, None]:
        """Provides an iterator for the SLL."""
        if not self.head:
            raise IndexError("The list empty, cannot create an iterator.")
        else:
            cursor: Node = self.head
            while cursor:
                yield cursor

                # Exit Condition
                if cursor == self.tail:
                    break

                # Loop Control Variable
                assert cursor.next, "Cursor's Next Pointer cannot be none in the middle of the iterator."
                cursor = cursor.next

    def __str__(self) -> str:
        """Provides a string repr for the TreeSLL."""
        repr_str: str = ""

        if not self.head:
            repr_str = "None <= Head\nNone <= Tail\n"
        else:
            for node in self:
                if node == self.head and node == self.tail:
                    repr_str += f"{node} <= Head\n{node} <= Tail\n"
                elif node == self.head:
                    repr_str += f"{node} <= Head\n"
                elif node == self.tail:
                    repr_str += f"{node} <= Tail\n"
                else:
                    repr_str += f"{node}\n"
        
        return repr_str
    
    # ==== Member Functions ====
    def append(self, value: Any) -> None:
        """Adds a new node to the end of the list."""
        new_node: Node = Node(value)

        # If the LL is empty.
        if not self.head:
            self.head = new_node
            self.tail = new_node
        # If the LL is not empty.
        else:
            assert self.tail, "Tail cannot be none in non empty SLL."
            self.tail.next = new_node
            self.tail = new_node
        
        # Updating the no of elements.
        self.no_of_elements += 1

    def pop_first(self) -> Node:
        """Removes the first element of the list and returns it."""
        remove_node: Node

        # If the LL is empty.
        if not self.head:
            raise IndexError("The list is empty, append elements before pop.")
        # If the LL is not empty.
        else:
            remove_node = self.head

            # If there is only one element in the list.
            if self.no_of_elements == 1:
                self.head = None
                self.tail = None
            # If there are more than one elements in the list.
            else:
                assert self.head.next, "The second element of the list cannot be none."
                next_node: Node = self.head.next

                # Updating the Head
                self.head = next_node

            # Updating the links of the remove node.
            remove_node.next = None

            # Updating the no of elements in the list.
            self.no_of_elements -= 1

            return remove_node

    def clear(self):
        """Clears the LL."""
        self.head = None
        self.tail = None
        self.no_of_elements = 0
from linear_structures.sll_tree import TreeNode, TreeSLL, Node
from typing import Any, Generator


class QueueTree:
    """Implements the behaviours of a Queue using the TreeNode structure."""
    # ==== Standard Methods ====
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.queue = TreeSLL()
        self.no_of_elements: int = 0

    def __str__(self) -> str:
        """Returns a string repr of the Queue."""
        return self.queue.__str__()
    
    def __iter__(self) -> Generator[Any, None, None]:
        """Returns an iterator for the Queue."""
        return self.queue.__iter__()
    
    # ==== Member Functions ====
    def enqueue(self, value: Any) -> None:
        """Adds a new node to the Queue."""
        new_tree_node: TreeNode = value
        
        # Adding the new tree node into the SLL
        self.queue.append(new_tree_node)

        # Updating the Queue Pointers
        if self.no_of_elements == 0:
            self.head = self.queue.head
        self.tail = self.queue.tail

        # Updating the Queue Element count
        self.no_of_elements += 1

    def dequeue(self) -> Node:
        """Removes the first node from the queue and returns it."""
        remove_node: Node = self.queue.pop_first()

        # Updating the pointers of the Queue
        if self.no_of_elements == 1:
            self.tail = None
            self.head = None
        else:
            self.head = self.queue.head

        # Updating the Queue Element count
        self.no_of_elements -= 1

        return remove_node

    def is_empty(self) -> bool:
        """Returns a boolean checking for an empty queue."""
        if self.no_of_elements == 0:
            return True
        return False
    
    def clear(self) -> None:
        """Clears the Queue."""
        self.head = None
        self.tail = None
        self.no_of_elements = 0
        self.queue.clear()

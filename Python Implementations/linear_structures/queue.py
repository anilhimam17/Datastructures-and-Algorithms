from linear_structures.sll import SLL, Node
from typing import Any


class Queue:
    """Implements the Queue Data Structure using a Linked List."""

    # ==== Standard Methods ====
    def __init__(self) -> None:
        
        self.head: Node | None = None
        self.tail: Node | None = None
        self.no_of_elements: int = 0
        self.queue = SLL()

    def __str__(self) -> str:
        """Provides a string representation for the Queue."""
        
        repr_str: str = ""

        # If the queue is empty.
        if not self.head:
            repr_str = "None <= Head\nNone <= Tail\n"
        # If the queue is not empty.
        else:
            for node in self.queue:
                if node == self.head:
                    repr_str += f"{node} <= Head\n"
                elif node == self.tail:
                    repr_str += f"{node} <= Tail\n"
                else:
                    repr_str += f"{node}\n"
        
        return repr_str
    
    # ==== Methods of the Queue =====
    def enqueue(self, value: Any) -> None:
        """Adds a new element to the end of the queue."""

        # If the queue is currently empty.
        if not self.head:
            self.queue.append(value)
            self.head = self.queue.head
            self.tail = self.queue.tail
        # If the queue is not empty
        else:
            self.queue.append(value)
            self.tail = self.queue.tail

        # Updating the no of elements in the queue
        self.no_of_elements += 1

    def dequeue(self) -> Node:
        """Removes the first node for the queue and returns it."""
        
        remove_node: Node

        # If the queue is empty
        if not self.head:
            raise IndexError("There are no nodes in the queue that can be popped.")
        # If the queue is not empty
        else:
            remove_node = self.queue.remove(0)
            self.head = self.queue.head

        # Updating the no of elements
        self.no_of_elements -= 1
        return remove_node
    
    def peek(self) -> Node:
        """Returns the top most node in the queue."""
        
        # If the queue is empty.
        if not self.head:
            raise IndexError("The queue is currently empty, enter new nodes.")
        # If the queue is not empty.
        else:
            return self.head
        
    def is_empty(self) -> bool:
        """Returns a boolean after checking for an empty queue."""
        
        if not self.head:
            return True
        return False
    
    def delete(self) -> None:
        """Deletes the current queue."""
        
        self.queue.clear()
        self.head = None
        self.tail = None
        self.no_of_elements = 0

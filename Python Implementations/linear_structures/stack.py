from linear_structures.sll import SLL, Node
from typing import Any


class Stack:
    def __init__(self) -> None:
        self.top: Node | None = None
        self.stack = SLL()
        self.no_of_elements = 0

    def __str__(self) -> str:
        """Provides a string repr for the stack."""
        str_repr: str = ""

        # If the stack is empty
        if not self.top:
            str_repr = "None <= Top\n"
        # If the stack is not empty
        else:
            for node in self.stack:
                if node == self.top:
                    str_repr += f"{node} <= Head\n"
                else:
                    str_repr += f"{node}\n"
        # Returning the string
        return str_repr

    def push(self, value: Any) -> None:
        """Append a new node to the top of the stack."""
        if self.no_of_elements == 0:
            self.stack.append(value)
        else:
            self.stack.insert(value, 0)

        # Updating the top of the stack.    
        self.top = self.stack.head

        # Updating the no of elements in the stack.
        self.no_of_elements += 1

    def pop(self) -> Node:
        """Returns the top most element of the stack."""
        if not self.top:
            raise IndexError("There are no remaining nodes in the stack that can be popped.")
        else:
            # Removing the top most element in the stack.
            popped_node: Node = self.stack.remove(0)

            # Updating the top pointer
            self.top = self.stack.head

            # Updating the no of elements in the stack.
            self.no_of_elements -= 1

            return popped_node
        
    def is_empty(self) -> bool:
        """Returns a boolean checking if the stack is empty."""
        if self.no_of_elements == 0 and not self.top:
            return True
        return False
        
    def peek(self) -> Node:
        """Returns the top most element in the stack."""
        if not self.is_empty():
            assert self.top, "The top of the stack cannot be none for when non-empty."
            return self.top
        else:
            raise IndexError("The stack is currently empty.")
        
    def delete(self) -> None:
        """Deletes the stack."""
        self.stack.clear()
        self.top = None
        self.no_of_elements = 0

        
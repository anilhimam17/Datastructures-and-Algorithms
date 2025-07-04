from typing import Any, Generator


class BinaryTree:
    """Implements the behaviour of a Binary Tree using a List."""
    # ==== Standard Methods ====
    def __init__(self, size: int = 10) -> None:
        self.last_used_index: int = 0
        self.list: list = [None] * (size + 1)
        self.no_of_elements: int = 0
        self.max_size = size

    def __str__(self) -> str:
        """Provides a string representation of the tree."""
        if self.no_of_elements == 0:
            raise IndexError("The tree is empty add elements before visualising.")
        return self.print_tree(1)
    
    def __iter__(self) -> Generator[Any, None, None]:
        """Provides an iterator for the representation of the tree."""
        for idx in range(1, self.last_used_index + 1):
            yield self.list[idx]
    
    @property
    def root(self) -> Any:
        """Gives dynamic access to the root element of the tree as it is filled."""
        if self.list[1] is None:
            return None
        else:
            return self.list[1]
        
    
    # ==== Helper Functions ====
    def print_tree(self, index: int, level: int = 0, label: str = "Root:") -> str:
        """Creates a pretty representation of the tree."""
        # Base Case.
        if index > self.last_used_index:
            return ""
        elif self.list[index] is None:
            return ""
        # Recursive Case.
        right = self.print_tree((2 * index) + 1, level + 1, label="R----")
        current = "          " * level + f"{label} {self.list[index]}\n"
        left = self.print_tree(2 * index, level + 1, "L----")

        # Accumulated Tree representation string.
        return right + current + left

    # ==== Member Functions ====
    def add_child(self, value: Any) -> None:
        """Adds a new child to the tree."""

        # If the tree is full.
        if self.no_of_elements + 1 > self.max_size:
            raise IndexError("The tree is full, please remove elements before appending.")
        
        # Finding the next available position and entering the element.
        self.last_used_index += 1
        self.list[self.last_used_index] = value
        self.no_of_elements += 1

    def remove_child(self, value: Any) -> None:
        """Removes a child from the tree."""
        for idx, element in enumerate(self):
            if element == value:
                self.list[idx + 1] = self.list[self.last_used_index]
                self.list[self.last_used_index] = None
                break
        else:
            raise IndexError("The requested element was not found.")
        
        # Updating the list specs
        self.last_used_index -= 1
        self.no_of_elements -= 1

    def search_child(self, value: Any) -> bool:
        """Searches for a value in the tree."""
        for element in self:
            if element == value:
                return True
        return False
    
    def update_child(self, value: Any, new_value: Any) -> None:
        """Update the value of a child on first occurence."""
        for idx in range(1, self.last_used_index + 1):
            if self.list[idx] == value:
                self.list[idx] = new_value
                break

    def preorder_traversal(self, index: int) -> None:
        """Preorder traversal for the Binary Tree."""
        if index > self.last_used_index:
            return
        print(self.list[index])
        self.preorder_traversal(2 * index)
        self.preorder_traversal(2 * index + 1)

    def inorder_traversal(self, index: int) -> None:
        """Inorder traversal for the Binary Tree."""
        if index > self.last_used_index:
            return
        self.inorder_traversal(2 * index)
        print(self.list[index])
        self.inorder_traversal(2 * index + 1)

    def postorder_traversal(self, index: int) -> None:
        """Postorder traversal for the Binary Tree."""
        if index > self.last_used_index:
            return
        self.postorder_traversal(2 * index)
        self.postorder_traversal(2 * index + 1)
        print(self.list[index])
            
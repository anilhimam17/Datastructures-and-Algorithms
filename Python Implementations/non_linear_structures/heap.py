from typing import Generator


class Heap:
    """Provides an implementation of the heap datastructure using Python Lists."""
    def __init__(self, heap_size: int, heap_type: str = "min") -> None:
        self.root = None
        self.heap_list: list[int | None] = [None] * (heap_size + 1)
        self.max_heap_size = heap_size
        self.current_heap_size = 1

    def __iter__(self) -> Generator[int | None, None, None]:
        """Provides a iterator for the Heap using Level Order traversal."""
        
        # If the heap is only containing None
        if self.heap_list is None:
            return None
            
        for i in range(1, self.current_heap_size + 1):
            yield self.heap_list[i]

    def __str__(self) -> str:
        """Provides a string representation of the Heap."""
        return self.print_tree(index=1)

    def print_tree(self, index: int, level: int = 0, label: str = "Root") -> str:
        """Provides a pretty printed string representation of the tree."""
        
        # Base Cases
        if index > self.current_heap_size:
            return ""
        if self.heap_list[index] is None:
            return ""
        
        # Recursive Case
        left = self.print_tree(index * 2, level=level+1, label="L-----")
        right = self.print_tree(index * 2 + 1, level=level+1, label="R-----")
        current = "        " * level + f"{label} {self.heap_list[index]}\n"

        return left + current + right

    def peek(self) -> int | None:
        """Returns the topmost element of the heap."""
        return self.root
    
    def insert(self, new_value: int) -> None:
        """Inserts a new element into the heap by following the standard of a BTree."""

        # Check Heap Size
        if not (self.current_heap_size + 1 <= self.max_heap_size):
            raise OverflowError("The max heap size has exceeded")

        # If the heap is empty
        if self.root is None:
            self.heap_list[self.current_heap_size] = new_value
            self.root = self.heap_list[1]
            self.current_heap_size += 1
            return
        
        for i in range(1, self.current_heap_size + 1):
            # If left child is empty
            if self.heap_list[i * 2] is None:
                self.heap_list[i * 2] = new_value
                break
            # If right child is empty
            elif self.heap_list[(i * 2) + 1] is None:
                self.heap_list[(i * 2) + 1] = new_value
                break
        
        # Updating the current heap size on insertion
        self.current_heap_size += 1
        return

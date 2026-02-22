from typing import Generator


class Heap:
    """Provides an implementation of the heap datastructure using Python Lists."""
    
    # ==== Standard Methods ====
    def __init__(self, heap_size: int, heap_type: str = "min") -> None:
        
        self.heap_list: list[int | None] = [None] * (heap_size + 1)
        self.max_heap_size = heap_size
        self.current_heap_size = 1
        self.heap_type = heap_type

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
    
    # ==== Helper Methods ====
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

        return right + current + left
    
    # ==== Member Methods ====
    def peek(self) -> int | None:
        """Returns the topmost element of the heap."""
        
        return self.heap_list[1]
    
    def insert(self, new_value: int) -> None:
        """Inserts a new element into the heap by following the standard of a BTree.
        Important:
        - Due to the direct swapping nature of Heapify a Heap may not adhere to all
        of the rules of a BTree especially left_child.value < root.value < right_child.value
        at all times."""

        # Check Heap Size
        if not (self.current_heap_size + 1 <= self.max_heap_size):
            raise OverflowError("The max heap size has exceeded")

        # If the heap is empty
        if self.heap_list[1] is None:
            self.heap_list[self.current_heap_size] = new_value
            self.current_heap_size += 1
            return
        
        # Traversing the Heap to find a vacancy before Heapify
        for i in range(1, self.current_heap_size + 1):
            # If left child is empty
            if self.heap_list[i * 2] is None:
                self.heap_list[i * 2] = new_value
                break
            # If right child is empty
            elif self.heap_list[(i * 2) + 1] is None:
                self.heap_list[(i * 2) + 1] = new_value
                break

        # Heapifying the insertion into the list
        self._heapify_insert(
            current_index=self.current_heap_size,
            heap_type=self.heap_type
        )
        
        # Updating the current heap size on insertion
        self.current_heap_size += 1
        return
    
    def _heapify_insert(self, current_index: int, heap_type: str) -> None:
        """Performs the Heapify operation to balance the nodes of the Heap
        after an insertion by Bubbling up the new value based on Heap Type."""

        # Accessing the Parent to Back-Track for any swaps necessary in the Hierarchy
        parent_index: int = current_index // 2

        # Base Case: At the level of root node with no other nodes in the heap
        if parent_index < 1:
            return

        # Checking the values to ensure not unbound
        assert isinstance(self.heap_list[parent_index], int), "Parent Node cannot be none in the middle of the Heap"
        assert isinstance(self.heap_list[current_index], int), "Current Node cannot be none after insertion"

        # If Min Heap
        if heap_type == "min" and (self.heap_list[parent_index] > self.heap_list[current_index]):  # type: ignore
            self.heap_list[parent_index], self.heap_list[current_index] = (
                self.heap_list[current_index], self.heap_list[parent_index]
            )
        # If Max Heap
        if heap_type == "max" and (self.heap_list[parent_index] < self.heap_list[current_index]):  #type: ignore
            self.heap_list[parent_index], self.heap_list[current_index] = (
                self.heap_list[current_index], self.heap_list[parent_index]
            )

        # Recursive Case: Heapifying the Swapped New Node further (if needed)
        self._heapify_insert(current_index=parent_index, heap_type=heap_type)
        return
    
    def extract(self) -> int:
        """Returns the root node after extracting it from the Heap. It then balances 
        the Heap through Heapify after choosing the deepest node in the Heap as the 
        successor for the extraction of root.

        Important:
        - In a Heap only the root node can be extracted and not just any sub-node."""

        # If the Heap is empty
        if self.heap_list[1] is None:
            raise IndexError("The Heap is empty, add elements before extraction")
        
        extract_node: int = 0

        # If only the root node in Heap
        if self.current_heap_size == 2:
            extract_node = self.heap_list[1]
            self.heap_list[self.current_heap_size - 1] = None
        # If more than one node in the Heap
        else:
            extract_node = self.heap_list[1]

            # Replacing the root with the deepest node
            self.heap_list[1] = self.heap_list[self.current_heap_size - 1]
            self.heap_list[self.current_heap_size - 1] = None

            # Heapifying to balance the new root node
            self._heapify_extract(current_index=1)
        
        # Updating the Heap Size
        self.current_heap_size -= 1
        return extract_node
    
    def _heapify_extract(self, current_index: int) -> None:
        """Performs the Heapify operation to balance the nodes of the Heap 
        after an extraction by Bubbling down the new value based on the Heap Type."""

        # Accessing the Parent
        parent = self.heap_list[current_index]

        # Accessing the Immediate Children from Root
        if current_index * 2 < self.current_heap_size - 1:
            left_child_idx = current_index * 2
            left_child = self.heap_list[left_child_idx]
        else:
            return
        if (current_index * 2) + 1 < self.current_heap_size - 1:
            right_child_idx = (current_index * 2) + 1
            right_child = self.heap_list[right_child_idx]
        else:
            return

        # Checking the values to ensure not unbound
        assert parent, "Parent cannot be none after checking heap size"

        # If Min Heap
        if self.heap_type == "min":
            # If both children are available
            if left_child and right_child:
                swap_child_idx = left_child_idx if left_child < right_child else right_child_idx
                swap_child = self.heap_list[swap_child_idx]
                if swap_child < parent:  # type: ignore
                    self.heap_list[current_index], self.heap_list[swap_child_idx] = (
                        self.heap_list[swap_child_idx], self.heap_list[current_index]
                    )

                    # Heapifying the Swapped New Node further (if needed)
                    self._heapify_extract(current_index=swap_child_idx)
            # If only one child is available
            else:
                swap_child_idx = left_child_idx if left_child_idx else right_child_idx
                swap_child = self.heap_list[swap_child_idx]
                if swap_child < parent:  # type: ignore
                    self.heap_list[current_index], self.heap_list[swap_child_idx] = (
                        self.heap_list[swap_child_idx], self.heap_list[current_index]
                    )

                    # Heapifying the Swapped New Node further (if needed)
                    self._heapify_extract(current_index=swap_child_idx)
        # If Max Heap
        elif self.heap_type == "max":
            # If both children are available
            if left_child and right_child:
                swap_child_idx = left_child_idx if left_child > right_child else right_child_idx
                swap_child = self.heap_list[swap_child_idx]
                if swap_child > parent:  # type: ignore
                    self.heap_list[current_index], self.heap_list[swap_child_idx] = (
                        self.heap_list[swap_child_idx], self.heap_list[current_index]
                    )

                    # Heapifying the Swapped New Node further (if needed)
                    self._heapify_extract(current_index=swap_child_idx)
            # If only one child is available
            else:
                swap_child_idx = left_child_idx if left_child_idx else right_child_idx
                swap_child = self.heap_list[swap_child_idx]
                if swap_child > parent:  # type: ignore
                    self.heap_list[current_index], self.heap_list[swap_child_idx] = (
                        self.heap_list[swap_child_idx], self.heap_list[current_index]
                    )

                    # Heapifying the Swapped New Node further (if needed)
                    self._heapify_extract(current_index=swap_child_idx)
        else:
            raise ValueError("Heap Type or Heap Structure is invalid")

        return


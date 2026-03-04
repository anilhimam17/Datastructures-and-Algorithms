from typing import Generator


class Heap[T]:
    """Provides an implementation of the heap datastructure using Python Lists."""
    
    # ==== Standard Methods ====
    def __init__(self, heap_size: int, heap_type: str = "min") -> None:
        
        self.heap_list: list[T | None] = [None] * (heap_size + 1)
        self.max_heap_size = heap_size
        self.current_heap_size = 1
        self.heap_type = heap_type

    def __iter__(self) -> Generator[T | None, None, None]:
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
        current = "             " * level + f"{label} {self.heap_list[index]}\n"

        return right + current + left
    
    # ==== Member Methods ====
    def peek(self) -> T | None:
        """Returns the topmost element of the heap."""
        
        return self.heap_list[1]
    
    def insert(self, new_value: T, key: int = 0) -> None:
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
        
        # If not empty add the new value to the last available spot before heapifying
        self.heap_list[self.current_heap_size] = new_value

        # Heapifying the insertion into the list
        self._heapify_insert(
            current_index=self.current_heap_size,
            heap_type=self.heap_type,
            key=key
        )
        
        # Updating the current heap size on insertion
        self.current_heap_size += 1
        return
    
    def extract(self, key: int = 0) -> T:
        """Returns the root node after extracting it from the Heap. It then balances 
        the Heap through Heapify after choosing the deepest node in the Heap as the 
        successor for the extraction of root.

        Important:
        - In a Heap only the root node can be extracted and not just any sub-node."""

        # If the Heap is empty
        if self.heap_list[1] is None:
            raise IndexError("The Heap is empty, add elements before extraction")
        
        # Extracting the root node
        extract_node: T = self.heap_list[1]

        # If only the root node in Heap
        if self.current_heap_size == 2:
            self.heap_list[self.current_heap_size - 1] = None
        # If more than one node in the Heap
        else:
            # Replacing the root with the deepest node
            self.heap_list[1] = self.heap_list[self.current_heap_size - 1]
            self.heap_list[self.current_heap_size - 1] = None

            # Heapifying to balance the new root node
            self._heapify_extract(current_index=1, key=key)
        
        # Updating the Heap Size
        self.current_heap_size -= 1
        return extract_node
    
    # ==== Helper Functions ====
    def _heapify_insert(self, current_index: int, heap_type: str, key: int = 0) -> None:
        """Performs the Heapify operation to balance the nodes of the Heap
        after an insertion by Bubbling up the new value based on Heap Type."""

        # Accessing the Parent to Back-Track for any swaps necessary in the Hierarchy
        parent_index: int = current_index // 2

        # Base Case: At the level of root node with no other nodes in the heap
        if parent_index < 1:
            return

        # Checking the values to ensure not unbound
        # If Min Heap
        if heap_type == "min":
            if key == 0 and (self.heap_list[parent_index] > self.heap_list[current_index]):  # type: ignore
                self.heap_list[parent_index], self.heap_list[current_index] = (
                    self.heap_list[current_index], self.heap_list[parent_index]
                )
                # Recursive Case: Heapifying the Swapped New Node further (if needed)
                self._heapify_insert(current_index=parent_index, heap_type=heap_type, key=key)
            # Using key-th index for comparison if iterables are values in the heap
            elif key > 0 and (self.heap_list[parent_index][key] > self.heap_list[current_index][key]):  # type: ignore
                self.heap_list[parent_index], self.heap_list[current_index] = (
                    self.heap_list[current_index], self.heap_list[parent_index]
                )
                # Recursive Case: Heapifying the Swapped New Node further (if needed)
                self._heapify_insert(current_index=parent_index, heap_type=heap_type, key=key)
        # If Max Heap
        if heap_type == "max":
            if key == 0 and (self.heap_list[parent_index] < self.heap_list[current_index]):  #type: ignore
                self.heap_list[parent_index], self.heap_list[current_index] = (
                    self.heap_list[current_index], self.heap_list[parent_index]
                )
                # Recursive Case: Heapifying the Swapped New Node further (if needed)
                self._heapify_insert(current_index=parent_index, heap_type=heap_type, key=key)
            # Using key-th index for comparison if iterables are values in the heap
            elif key > 0 and (self.heap_list[parent_index][key] < self.heap_list[current_index][key]):  #type: ignore
                self.heap_list[parent_index], self.heap_list[current_index] = (
                    self.heap_list[current_index], self.heap_list[parent_index]
                )
                # Recursive Case: Heapifying the Swapped New Node further (if needed)
                self._heapify_insert(current_index=parent_index, heap_type=heap_type, key=key)
        return
    
    def _heapify_extract(self, current_index: int, key: int = 0) -> None:
        """Performs the Heapify operation to balance the nodes of the Heap 
        after an extraction by Bubbling down the new value based on the Heap Type."""

        # Accessing the Parent
        parent = self.heap_list[current_index]
        
        # Accessing the Immediate Children from Root for swap candidates
        candidates = []

        # If Left Child in bound and exists
        if (
            current_index * 2 < self.current_heap_size and 
            self.heap_list[current_index * 2] is not None
        ):
            swap_index = current_index * 2
            candidates.append([self.heap_list[swap_index], swap_index])
        # If Right Child in bound and exists
        if (
            (current_index * 2) + 1 < self.current_heap_size and 
            self.heap_list[(current_index * 2) + 1] is not None
        ):
            swap_index = (current_index * 2) + 1
            candidates.append([self.heap_list[swap_index], swap_index])
        
        # If candidates is empty reach leaf node
        if not candidates:
            return

        # Finalising the Swap Candidate
        if self.heap_type == "min":
            if key == 0:
                swap_item = min(candidates, key=lambda x: x[0])
            else:
                swap_item = min(candidates, key=lambda x: x[0][key])
        else:
            if key == 0:
                swap_item = max(candidates, key=lambda x: x[0])
            else:
                swap_item = max(candidates, key=lambda x: x[0][key])
        
        # Accessing the Swap Child Value and Index for Heapifying
        swap_child, swap_child_idx = swap_item

        # If Min Heap
        if self.heap_type == "min":
            # If the values in the Heap are literals
            if key == 0 and swap_child < parent:
                self.heap_list[current_index], self.heap_list[swap_child_idx] = (
                    self.heap_list[swap_child_idx], self.heap_list[current_index]
                )
                # Heapifying the Swapped New Node further (if needed)
                self._heapify_extract(current_index=swap_child_idx, key=key)
            # If the values in the Heap are iterables
            if key != 0 and swap_child[key] < parent[key]:  # type: ignore
                self.heap_list[current_index], self.heap_list[swap_child_idx] = (
                    self.heap_list[swap_child_idx], self.heap_list[current_index]
                )
                # Heapifying the Swapped New Node further (if needed)
                self._heapify_extract(current_index=swap_child_idx, key=key)
        # If Max Heap
        elif self.heap_type == "max":
            # If the values in the Heap are literals
            if key == 0 and swap_child > parent:
                self.heap_list[current_index], self.heap_list[swap_child_idx] = (
                    self.heap_list[swap_child_idx], self.heap_list[current_index]
                )
                # Heapifying the Swapped New Node further (if needed)
                self._heapify_extract(current_index=swap_child_idx, key=key)
            # If the values in the Heap are iterables
            if key != 0 and swap_child[key] > parent[key]:  # type: ignore
                self.heap_list[current_index], self.heap_list[swap_child_idx] = (
                    self.heap_list[swap_child_idx], self.heap_list[current_index]
                )
                # Heapifying the Swapped New Node further (if needed)
                self._heapify_extract(current_index=swap_child_idx, key=key)
        else:
            raise ValueError("Heap Type or Heap Structure is invalid")

        return

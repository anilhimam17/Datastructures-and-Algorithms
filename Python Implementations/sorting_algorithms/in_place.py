from collections.abc import Callable
import operator
import random


class InPlace:
    """This class implements the semantic structure 
    that house In-Place Sorting Algorithms."""

    @staticmethod
    def resolve_sorting_method(method_name: str) -> Callable[[list, str], list]:
        """Retrieves the appropriate sorting algorithm based on the provide method_name 
        and returns the callable to it."""

        if method_name == "bubble_sort":
            return InPlace.bubble_sort
        elif method_name == "selection_sort":
            return InPlace.selection_sort
        elif method_name == "insertion_sort":
            return InPlace.insertion_sort
        elif method_name == "quick_sort":
            return InPlace.quick_sort
        else:
            raise ValueError("The provided method name was invalid")

    @staticmethod
    def bubble_sort(input_list: list, order: str = "ascending") -> list:
        """Performs bubble sort on the input list and returns the sorted list."""

        if order not in ["ascending", "descending"]:
            raise ValueError("The order string provided was invalid")
        elif order == "ascending":
            comparator = operator.gt
        else:
            comparator = operator.lt

        list_size = len(input_list)

        # Outer Loop to orchestrate the comparisions
        for i in range(list_size - 1):
            # Inner Loop to apply pair-wise comparisions with bubbling limit
            # - i applied to not disturb already bubbled elements (Bubbling Limit)
            # - 1 applied to avert out of bound error during last element comparison

            # Early stopping flag
            swapped = False
            for j in range(list_size - i - 1):    
                if comparator(input_list[j], input_list[j + 1]):
                    input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                    swapped = True
                
            # If no swaps have taken place list is sorted
            if not swapped:
                break
        
        return input_list
    
    @staticmethod
    def selection_sort(input_list: list, order: str = "ascending") -> list:
        """Performs selection sort on the input list and returns the sorted list."""

        if order not in ["ascending", "descending"]:
            raise ValueError("The order string provided was invalid")
        elif order == "ascending":
            comparator = operator.lt
        else:
            comparator = operator.gt

        list_size = len(input_list)

        # Outer Loop to orcheste the comparisons
        for i in range(list_size):
            
            # Inner Loop to find the min / max elements for each iteration
            swap_index = i
            
            # Start from the ith index to not disturb the already sorted part
            # + 1 applied to search all but the initial element as potential swap cases
            for j in range(i + 1, list_size):
                if comparator(input_list[j], input_list[swap_index]):
                    swap_index = j

            # Swapping the selected element for the current iteration
            input_list[i], input_list[swap_index] = input_list[swap_index], input_list[i]

        return input_list
    
    @staticmethod
    def insertion_sort(input_list: list, order: str = "ascending") -> list:
        """Performs insertion sort on the input list and returns the sorted list."""

        if order not in ["ascending", "descending"]:
            raise ValueError("The order string provided was invalid")
        elif order == "ascending":
            comparator = operator.lt
        else:
            comparator = operator.gt
        
        list_size = len(input_list)

        # Outer Loop to iterate through the unsorted list for insertion into the sorted part
        for i in range(1, list_size):
            # Inner Loop to insert the element into the correct position
            for j in range(i):
                if comparator(input_list[i], input_list[j]):
                    # Inserting the element at the correct location in sorted part
                    input_list.insert(j, input_list[i])
                    # Removing the element from the unsorted part
                    input_list.pop(i + 1)
                    break

        return input_list

    @staticmethod
    def quick_sort(input_list: list, order: str = "ascending") -> list:
        """Performs the quick sort algorithm on the elements in place thereby returning 
        the reference to the list."""

        if order not in ["ascending", "descending"]:
            raise ValueError("The Provide input for order type is invalid")
        
        input_list = InPlace._quick_sort_engine(
            input_list=input_list,
            low=0,
            high=len(input_list) - 1,
            order=order
        )

        return input_list
        
    @staticmethod
    def _quick_sort_engine(input_list: list, low: int, high: int, order: str) -> list:
        """Initiates the recursion call stack to partition and sort the list using quick sort."""
        
        # Recursive Case: If there exists a range between low and high continue parititioning and sort
        if low < high:
            # First Pivot Index
            pivot_index = InPlace._quick_sort_helper(
                input_list=input_list,
                low=low,
                high=high,
                order=order
            )

            # Recursively Calling the Quick Sort helper for partitions around pivot index
            # Sorting the Left Side Partition
            InPlace._quick_sort_engine(
                input_list=input_list,
                low=low,
                high=pivot_index - 1,
                order=order
            )
            # Sorting the Right Side Partition
            InPlace._quick_sort_engine(
                input_list=input_list,
                low=pivot_index + 1,
                high=high,
                order=order
            )
        
        # Base Case: Return list if list size = 1 where low == high
        return input_list

    @staticmethod
    def _quick_sort_helper(input_list: list, low: int, high: int, order: str) -> int:
        """Performs the swapping of elements in the input list in accordance to the pivot element.
        It then returns index location for the Pivot element for downstream sorts."""

        if order == "ascending":
            comparator = operator.le
        else:
            comparator = operator.ge
        
        # Calculating a randomised pivot element
        pivot_idx = random.randint(low, high)
        input_list[high], input_list[pivot_idx] = input_list[pivot_idx], input_list[high]
        pivot_element = input_list[high]

        # Boundary Index which will reduce to pivot index at the end of pair-wise swapping
        boundary_index = low - 1

        # Iterating through the partition to order the elements in accordance to Pivot using comparator
        for i in range(low, high):
            if comparator(input_list[i], pivot_element):
                # Updating the new boundary
                boundary_index += 1
                input_list[boundary_index], input_list[i] = input_list[i], input_list[boundary_index]
        
        # Moving the pivot into order
        input_list[boundary_index + 1], input_list[high] = (
            input_list[high],
            input_list[boundary_index + 1]
        )

        return boundary_index + 1
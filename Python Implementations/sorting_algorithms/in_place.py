from collections.abc import Callable
import operator


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


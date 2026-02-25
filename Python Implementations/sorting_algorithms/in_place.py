from collections.abc import Callable


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
        else:
            raise ValueError("The provided method name was invalid")

    @staticmethod
    def bubble_sort(input_list: list, order: str = "ascending") -> list:
        """Performs bubble sort on the input list and returns the sorted list."""

        if order not in ["ascending", "descending"]:
            raise ValueError("The order string provided was invalid")

        list_size = len(input_list)

        # Outer Loop to orchestrate the comparisions
        for i in range(list_size - 1):
            # Inner Loop to apply pair-wise comparisions with bubbling limit
            # - i applied to not disturb already bubbled elements (Bubbling Limit)
            # - 1 applied to avert out of bound error during last element comparison
            for j in range(list_size - i - 1):
                if order == "ascending" and input_list[j] > input_list[j + 1]:
                    input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                elif order == "descending" and input_list[j] < input_list[j + 1]:
                    input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                else: 
                    continue
        
        return input_list
    
    @staticmethod
    def selection_sort(input_list: list, order: str = "ascending") -> list:
        """Performs selection sort on the input list and returns the sorted list."""

        if order not in ["ascending", "descending"]:
            raise ValueError("The order string provided was invalid")

        list_size = len(input_list)

        # Outer Loop to orcheste the comparisons
        for i in range(list_size):
            
            # Inner Loop to find the min / max elements for each iteration
            swap_index = i
            
            # Start from the ith index to not disturb the already sorted part
            # + 1 applied to search all but the initial element as potential swap cases
            for j in range(i + 1, list_size):
                if order == "ascending" and input_list[j] < input_list[swap_index]:
                    swap_index = j
                elif order == "descending" and input_list[j] > input_list[swap_index]:
                    swap_index = j
                else:
                    continue
            
            # Swapping the selected element for the current iteration
            input_list[i], input_list[swap_index] = input_list[swap_index], input_list[i]

        return input_list


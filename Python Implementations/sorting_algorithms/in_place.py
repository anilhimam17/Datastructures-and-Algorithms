class InPlace:
    """This class implements the semantic structure 
    that house In-Place Sorting Algorithms."""

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
        
        return input_list

from collections.abc import Callable
from typing import Any


class SimpleSearch:
    """This class implements basic search algorithms which are not
    specialised to any particular data structure."""

    def resolve_search_method(self, method_name: str) -> Callable[[list, Any], int]:
        """Resolves the search algorithm required by name an returns a 
        callable to the corresponding method."""

        if method_name == "linear_search":
            return SimpleSearch.linear_search
        elif method_name == "binary_search":
            return SimpleSearch.binary_search
        else:
            raise ValueError("The given method name could not be found in Simple Search.")

    @staticmethod
    def linear_search(input_list: list, search_ele: Any) -> int:
        """Performs linear search on a list for search element and returns the index else -1."""
        
        # Traversing the list linearly
        for idx, ele in enumerate(input_list):
            if ele == search_ele:
                return idx
        return -1
    
    @staticmethod
    def binary_search(input_list: list, search_ele: Any) -> int:
        """Orchestrates the recursive binary search."""

        if not input_list:
            raise ValueError("The provided input list was invalid or empty.")
        
        res = SimpleSearch._binary_search_helper(
            input_list=input_list,
            search_ele=search_ele,
            low=0,
            high=len(input_list) - 1
        )

        return res
        
    @staticmethod
    def _binary_search_helper(input_list: list, search_ele: Any, low: int, high: int) -> int:
        """Performs binary search on a list for search element and returns the index else -1."""

        if low > high:
            return -1
        
        mid = (low + high) // 2
        if input_list[mid] == search_ele:
            return mid
        elif input_list[mid] > search_ele:
            return SimpleSearch._binary_search_helper(
                input_list=input_list, 
                search_ele=search_ele,
                low=low,
                high=mid-1
            )
        else:
            return SimpleSearch._binary_search_helper(
                input_list=input_list, 
                search_ele=search_ele,
                low=mid+1,
                high=high
            )
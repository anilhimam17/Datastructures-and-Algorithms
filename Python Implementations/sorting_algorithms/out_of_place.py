from __future__ import annotations
from collections.abc import Callable

import math


class OutOfPlace:
    """The class implements the semantic structure that house Out-Of-Place
    sorting algorithms."""
    
    def __init__(self, auxilary_sort_algo: Callable[[list, str], list]) -> None:
        self.auxilary_sort_algo = auxilary_sort_algo

    def resolve_method_name(self, method_name: str) -> Callable[[OutOfPlace, list, str], list]:
        """Resolves the sorting method to be used by name and returns the callable."""

        if method_name == "bucket_sort":
            return OutOfPlace.bucket_sort
        else:
            raise ValueError("The provided method name for the sorting algorithm is invalid.")
    
    def bucket_sort(self, input_list: list, order: str) -> list:
        """Performs bucket sort on the input list and returns the sorted list in-place."""
        
        # Algorithm-Level params
        list_size = len(input_list)

        # Accessing the operator for sorting
        if order not in ["ascending", "descending"]:
            raise ValueError("The provide order type is invalid")
        
        # Calculating the no of buckets
        n_buckets = math.ceil(math.sqrt(list_size))
        
        # Setting the bucket calculation constant
        bucket_id_const = n_buckets / max(input_list)

        # Creating the buckets
        bucket_list = [[] for _ in range(n_buckets)]
        
        # Assigning the elements to the buckets
        for ele in input_list:
            # Calculating the bucket for the element
            bucket_id = math.ceil((ele + 1e-6) * bucket_id_const)
            
            # Bounds checking the bucket id
            if bucket_id < 0:
                bucket_list[0].append(ele)
            elif bucket_id > n_buckets:
                bucket_list[n_buckets - 1].append(ele)
            else:
                bucket_list[bucket_id - 1].append(ele)

        # Peforming the sort operation on the buckets and merging them
        sorted_array = []
        sort_algo = self.auxilary_sort_algo

        for bucket_id in range(n_buckets):
            sort_algo(bucket_list[bucket_id], "ascending")
            sorted_array.extend(bucket_list[bucket_id])

        if order == "descending":
            return list(reversed(sorted_array))

        return sorted_array


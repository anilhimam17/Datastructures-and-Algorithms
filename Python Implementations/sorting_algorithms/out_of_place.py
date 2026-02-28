from __future__ import annotations
from collections.abc import Callable

import math
import operator

from non_linear_structures.heap import Heap


class OutOfPlace:
    """The class implements the semantic structure that house Out-Of-Place
    sorting algorithms."""
    
    def __init__(self, auxilary_sort_algo: Callable[[list, str], list]) -> None:
        self.auxilary_sort_algo = auxilary_sort_algo

    def resolve_method_name(self, method_name: str) -> Callable[[list, str], list]:
        """Resolves the sorting method to be used by name and returns the callable."""

        if method_name == "bucket_sort":
            return self.bucket_sort
        elif method_name == "merge_sort":
            return self.merge_sort
        elif method_name == "heap_sort":
            return self.heap_sort
        else:
            raise ValueError("The provided method name for the sorting algorithm is invalid.")
    
    def bucket_sort(self, input_list: list, order: str) -> list:
        """Performs bucket sort on the input list and returns the sorted list."""
        
        # Algorithm-Level params
        list_size = len(input_list)

        # Accessing the operator for sorting
        if order not in ["ascending", "descending"]:
            raise ValueError("The provided order type is invalid")
        
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
        
        # If order required is descending then reversed the sorted increasing list
        if order == "descending":
            return list(reversed(sorted_array))

        return sorted_array

    def merge_sort(self, input_list: list, order: str) -> list:
        """Performs merge sort on the input list and returns the sorted list."""

        # Recursion Control Parameter
        list_size = len(input_list)

        # Base Case: When a list can no longer be divided
        if list_size == 1:
            return input_list
        
        # Recursive Case: When a list can be divided further
        mid_point = list_size // 2
        list_partition_left = self.merge_sort(input_list=input_list[:mid_point], order=order)
        list_partition_right = self.merge_sort(input_list=input_list[mid_point:], order=order)

        # Sorting and Merging the partitions during backtracking
        merged_list = []
        merged_list.extend(
            OutOfPlace._merge_helper(
                left_list=list_partition_left, 
                right_list=list_partition_right, 
                order=order
            )
        )

        return merged_list

    @staticmethod
    def _merge_helper(left_list: list, right_list: list, order: str) -> list:
        """Helper method to aid merge sort by sort the partitions of the list 
        and merging them back into a single 1D list."""

        if order == "ascending":
            comparator = operator.lt
        else:
            comparator = operator.gt

        # Accessing the lengths of the partitions to bound the merging
        len_left, len_right = len(left_list), len(right_list)
        
        # The merged list that will comprise sorted elements from both partitions
        merged_list = []

        # Loop control variables
        i, j = 0, 0
        while True:
            # Control entry for merging until squarely even for ragged partitions
            if i < len_left and j < len_right:
                # Update Left List pointer if left list item < right list item
                if comparator(left_list[i], right_list[j]):
                    merged_list.append(left_list[i])
                    i += 1
                # Update Right List pointer viz.
                else:
                    merged_list.append(right_list[j])
                    j += 1
            # Exit loop if no longer square for pairwise comparison
            else:
                break
        
        # Extending the list with any remaining elements
        if order == "ascending":
            merged_list.extend(left_list[i:])
            merged_list.extend(right_list[j:])
        else:
            merged_list.extend(right_list[j:])
            merged_list.extend(left_list[i:])
        
        return merged_list

    def heap_sort(self, input_list: list, order: str) -> list:
        """Performs heap sort on the input list by leveraging the Binary Heap Tree
        sourced in the non_linear structures module and returns the input list."""

        sorted_list = []
        
        # Min Heap
        heap_type = "min" if order == "ascending" else "max"
        heap_ = Heap(heap_size=len(input_list) + 1, heap_type=heap_type)
        
        # Inserting the elements into the Heap
        for ele in input_list:
            heap_.insert(ele)
        
        # Inserting the elements into the Heap
        for _ in input_list:
            sorted_list.append(heap_.extract())

        return sorted_list

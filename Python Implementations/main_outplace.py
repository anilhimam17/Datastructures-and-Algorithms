import random
import time

from sorting_algorithms.in_place import InPlace
from sorting_algorithms.out_of_place import OutOfPlace


def main() -> None:

    # Instance of the Out of Place Sorting object
    sort_handle = OutOfPlace(auxilary_sort_algo=InPlace.insertion_sort)

    # Randomised list of elements for sorting
    input_list = [i for i in range(100000)]
    random.shuffle(input_list)

    print("\nList before sorting first 50 of 100000 elements:")
    print(input_list[:50])
    
    # Sort Algorithm names
    sort_algorithms = ["bucket_sort", "merge_sort", "heap_sort"]

    # Dictionary to store the performance of the sort algorithms
    sort_performance = {}

    # Iterating through the sorting algorithms to analyse performance
    for algo_name in sort_algorithms:
        
        print(f"\n{algo_name}")

        # Accessing the sort algo
        sort_algo = sort_handle.resolve_method_name(method_name=algo_name)
        
        # Performing sorting in ascending order
        print(f"\nSorting Ascending Order: {algo_name}")
        st_1 = time.time()
        ascending_list = sort_algo(input_list, "ascending")
        et_1 = time.time()
        
        # Checking the sort
        if not all(ascending_list[i] <= ascending_list[i + 1] for i in range(len(ascending_list) - 1)):
            raise ValueError("The list was not properly sorted in ascending order.")
        print("\nFirst 50 elements of the sorted array:")
        print(ascending_list[:50])

        # Performing sorting in descending order
        print(f"\nSorting Descending Order: {algo_name}")
        st_2 = time.time()
        descending_list = sort_algo(input_list, "descending")
        et_2 = time.time()

        if not all(descending_list[i] >= descending_list[i + 1] for i in range(len(descending_list) - 1)):
            raise ValueError("The list was not properly sorted in descending order.")
        print("\nFirst 50 elements of the sorted array:")
        print(descending_list[:50])

        avg_time = ((et_2 - st_2) + (et_1 - st_1)) / 2
        sort_performance[algo_name] = avg_time

    # Viewing the performance of the algorithms
    print("\nSorting performance of the algorithms")
    for item in sort_performance.items():
        print(item)


if __name__ == "__main__":
    main()
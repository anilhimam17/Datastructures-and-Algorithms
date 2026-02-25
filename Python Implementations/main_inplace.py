import random
import time

from sorting_algorithms.in_place import InPlace


def main() -> None:

    input_list = [i for i in range(10000)]
    random.shuffle(input_list)

    print("\nList before sorting first 50 of 10000 elements:")
    print(input_list[:50])

    # Initialsing the InPlace Sorting Handler
    sort_handle = InPlace()

    # Dict to store sort times
    sort_performance = {}

    # Iterating through the sorting algorithms
    sorting_algorithms = ["bubble_sort", "selection_sort"]
    for algo_name in sorting_algorithms:

        # Accessing the Sorting Algorithm
        sort_algo = sort_handle.resolve_sorting_method(method_name=algo_name)
        print(f"\nApplying {algo_name}")

        # Applying the Sorting Algorithm for Ascending Order
        st_1 = time.time()
        ascending_list = sort_algo(input_list, "ascending")
        et_1 = time.time()

        # Checking the sorted list
        if not all(ascending_list[i] < ascending_list[i + 1] for i in range(len(ascending_list) - 1)):
            raise ValueError(f"Ascending List for {algo_name} wasn't sorted")
        
        # Viewing the first 50 elements
        print(f"\nIn Ascending Order {algo_name}:")
        print(ascending_list[:50])
        
        # Applying the Sorting Algorithm for Descending Order
        st_2 = time.time()
        descending_list = sort_algo(input_list, "descending")
        et_2 = time.time()
        
        # Checking the sorted list
        if not all(descending_list[i] > descending_list[i + 1] for i in range(len(descending_list) - 1)):
            raise ValueError(f"Descending List for {algo_name} wasn't sorted")
        
        # Viewing the first 50 elements
        print(f"\nIn Descending Order {algo_name}:")
        print(descending_list[:50])
        
        # Calculating the average performance time for the algorithm
        avg_time = ((et_1 - st_1) + (et_2 - st_2)) / 2
        sort_performance[algo_name] = avg_time
    
    # Viewing the performance of the respective sorting algorithms
    print("\nAverage Sorting Times of the respective algorithms was:")
    for item in sort_performance.items():
        print(item)


if __name__ == "__main__":
    main()

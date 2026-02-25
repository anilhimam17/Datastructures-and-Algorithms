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

        # Applying the Sorting Algorithm
        st_1 = time.time()
        ascending_list = sort_algo(input_list, "ascending")
        print(f"\nIn Ascending Order {algo_name}:")
        print(ascending_list[:50])
        et_1 = time.time()

        st_2 = time.time()
        descending_list = sort_algo(input_list, "descending")
        print(f"\nIn Descending Order {algo_name}:")
        print(descending_list[:50])
        et_2 = time.time()

        avg_time = ((et_1 - st_1) + (et_2 - st_2)) / 2
        sort_performance[algo_name] = avg_time

    print("\nAverage Sorting Times of the respective algorithms was:")
    for item in sort_performance.items():
        print(item)


if __name__ == "__main__":
    main()

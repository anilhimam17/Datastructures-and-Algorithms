from collections import defaultdict
import random
import time

from searching_algorithms.simple_search import SimpleSearch


def main() -> None:

    # A sorted list to be search
    input_list = [i for i in range(100000)]
    
    # Search Algorithm to benchmark
    search_algo = ["linear_search", "binary_search"]

    # Search Handle
    search_handle = SimpleSearch()

    search_performance = defaultdict(list)
    for algo_name in search_algo:
        
        # Accessing the Callable to the method
        search_algo = search_handle.resolve_search_method(method_name=algo_name)
        
        # Benchmarking the performance on 5 runs
        for i in range(5):

            # Randomised Search element
            search_element = input_list[random.randint(0, len(input_list))]
            
            st = time.time()
            res = search_algo(input_list, search_element)
            et = time.time()
            
            search_delta = et - st
            search_performance[algo_name].append(search_delta)
            print(f"\n{algo_name} run {i + 1}")
            if res < 0:
                print(f"The search element was not found by {algo_name} and took {search_delta}")
            else:
                print(f"Search Element: {search_element} Element List Index: {res} and took {search_delta}")

    print("\n\nSearch Performance Analysis")
    for item in search_performance.items():
        mean_pref = round(sum(item[1]) / len(item[1]), 5)
        print(item[0], mean_pref)


if __name__ == "__main__":
    main()
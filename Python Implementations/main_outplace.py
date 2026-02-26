import random
import time

from sorting_algorithms.in_place import InPlace
from sorting_algorithms.out_of_place import OutOfPlace


def main() -> None:

    sort_handle = OutOfPlace(auxilary_sort_algo=InPlace.insertion_sort)

    input_list = [i for i in range(10000)]
    random.shuffle(input_list)

    st_1 = time.time()
    ascending_list = sort_handle.bucket_sort(input_list=input_list, order="ascending")
    et_1 = time.time()

    if not all(ascending_list[i] < ascending_list[i + 1] for i in range(len(ascending_list) - 1)):
        raise ValueError("The list was not properly sorted in ascending order.")
    print("\nFirst 50 elements of the sorted array:")
    print(ascending_list[:50])

    st_2 = time.time()
    descending_list = sort_handle.bucket_sort(input_list=input_list, order="descending")
    et_2 = time.time()

    if not all(descending_list[i] > descending_list[i + 1] for i in range(len(descending_list) - 1)):
        raise ValueError("The list was not properly sorted in descending order.")
    print("\nFirst 50 elements of the sorted array:")
    print(descending_list[:50])

    avg_time = ((et_2 - st_2) + (et_1 - st_1)) / 2
    print("Average Sort Time: ", avg_time)


if __name__ == "__main__":
    main()
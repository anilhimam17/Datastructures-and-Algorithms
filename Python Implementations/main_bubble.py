import random

from sorting_algorithms.in_place import InPlace


def main() -> None:

    input_list = [i for i in range(10)]
    random.shuffle(input_list)

    print("List before sorting:")
    print(input_list)

    sort_handle = InPlace()
    ascending_list = sort_handle.bubble_sort(input_list=input_list, order="ascending")
    print("\nIn Ascending Order:")
    print(ascending_list)

    descending_list = sort_handle.bubble_sort(input_list=input_list, order="descending")
    print("\nIn Descending Order:")
    print(descending_list)


if __name__ == "__main__":
    main()
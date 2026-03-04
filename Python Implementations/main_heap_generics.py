from non_linear_structures.heap import Heap


# The Main Function
def main() -> None:
    # Default Heap Testing
    print("\nCreating a Generic Min-Heap of Type Int")
    int_heap = Heap(heap_size=50)

    print("\nInserting 10 integers into the Heap")
    for i in range(1, 11):
        int_heap.insert(new_value=i)

    print(f"\nViewing the Type of the Heap after Insertion: {type(int_heap.heap_list)}")
    print(f"Viewing the Type of the Heap after Insertion: {type(int_heap.peek())}")
    print(f"The Min-Heap:\n{int_heap}")

    # Generic Heap Type and Custom Key Testing
    print("\nCreating a Generic Max-Heap of Type Tuple[str, int] with Custom Key")
    tuple_heap = Heap(heap_size=50, heap_type="max")

    print("\nInserting 10 tuple[Char, Int] pairs into the Heap")
    for i in range(1, 11):
        tuple_heap.insert(new_value=(chr(i + 65), i), key=1)

    print(f"\nViewing the Type of the Heap after Insertion: {type(tuple_heap.heap_list)}")
    print(f"Viewing the Type of the Heap after Insertion: {type(tuple_heap.peek())}")
    print(f"The Max-Heap:\n{tuple_heap}")

    # Generic Heap Type and Default Key Testing
    print("\nCreating a Generic Max-Heap of Type Tuple[str, int] with Default Key")
    def_heap = Heap(heap_size=50, heap_type="min")

    print("\nInserting 10 tuple[Char, Int] pairs into the Heap")
    for i in range(1, 11):
        def_heap.insert(new_value=(chr(i + 65), i))

    print(f"\nViewing the Type of the Heap after Insertion: {type(def_heap.heap_list)}")
    print(f"Viewing the Type of the Heap after Insertion: {type(def_heap.peek())}")
    print(f"The Max-Heap:\n{def_heap}")


# Driver Code
if __name__ == "__main__":
    main()

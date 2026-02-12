from non_linear_structures.heap import Heap


# The main function
def main():
    first_heap = Heap(heap_size=10, heap_type="max")
    
    print("Traversing the empty heap:")
    for i in first_heap:
        print(i)

    print("\nAdding 5 new elements")
    for i in range(1, 5):
        first_heap.insert(i)
        print(f"\nInserted Node: {i}")
        print("Tree after insertion")
        print(f"Root by structure: {first_heap.root}")
        print(first_heap)

    print("\nHeap List after all the insertions")
    print(first_heap.heap_list)

    print("\nHeap Structure after all the insertions")
    print(first_heap)

    for i in range(2):
        print(f"\nExtracting the {i + 1} root node: {first_heap.extract()}")
        print("\nThe Heap after extraction")
        print(f"Root by structure: {first_heap.root}")
        print(first_heap)
    
    print("\nHeap after all the extractions")
    print(first_heap)

    print("\nAdding 4 new elements")
    for i in range(1, 5):
        first_heap.insert(i * 10)
        print(f"\nInserted Node: {i * 10}")
        print("Tree after insertion")
        print(f"Root by structure: {first_heap.root}")
        print(first_heap)

    print("\nHeap after all the insertions")
    print(first_heap)
    print(f"Top most element: {first_heap.peek()}")

    print("\nRemoving all the elements")
    for i in range(6):
        print(f"\nExtracting the {i + 1} root node: {first_heap.extract()}")
        print("\nThe Heap after extraction")
        print(f"Root by structure: {first_heap.peek()}")
        print(first_heap)
    
    print("\nHeap after all the extractions")
    print(first_heap)


# Driver code
if __name__ == "__main__":
    main()
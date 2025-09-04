from non_linear_structures.heap import Heap


# The main function
def main():
    first_heap = Heap(10)
    
    print("Traversing the empty heap:")
    for i in first_heap:
        print(i)

    print("Adding 7 new elements")
    for i in range(1, 8):
        first_heap.insert(i)
    print(first_heap.heap_list)
    print(first_heap)


# Driver code
if __name__ == "__main__":
    main()
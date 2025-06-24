from linear_structures.sll import SLL

# Driver Code
def main() -> None:
    # Instantiating the SLL.
    sll = SLL()
    print("Current Elements in SLL:")
    print(sll)

    # Appending elements into the SLL.
    sll.append(10)
    print("Current Elements in SLL:")
    print(sll)
    sll.append(20)
    print("Current Elements in SLL:")
    print(sll)

    # Inserting elements into the SLL.
    sll.insert(1000, 0)
    print("Current Element in SLL:")
    print(sll)
    sll.insert(1000, 3)
    print("Current Element in SLL:")
    print(sll)
    sll.insert(1000, 2)
    print("Current Element in SLL:")
    print(sll)

    # Searching for an element.
    print("Found") if sll.search(10) else print("Not Found")
    print("Found") if sll.search(100) else print("Not Found")

    # Acessing elements
    for i in range(sll.no_of_elements):
        print(f"Element {i}: ", sll.get(i))

    # Updating the elements
    idx = int(input("Enter Index: "))
    inp = int(input("Enter Value: "))
    sll.set(idx, inp)
    print("Here is the updated list after the set op:")
    print(sll)

    # Popping elements
    popped = sll.pop()
    print("Here is the list of elements after pop:")
    print(sll)
    print("Popped element: ", popped)

    # Remove elements
    inp = int(input("Enter index to remove element: "))
    sll.remove(inp)
    print("Here is the list of elements after remove op: ")
    print(sll)

    # Iterating through all the elements
    print("Here is a traversal of the nodes in the linked list:")
    for node in sll:
        print(node)

    # Clear elements
    sll.clear()
    print("Here is the cleared SLL.")
    print(sll)

if __name__ == "__main__":
    main()

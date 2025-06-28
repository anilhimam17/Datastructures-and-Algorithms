from linear_structures.csll import CSLL
from linear_structures.csll import Node


# ==== Main Function ====
def main():
    first_node = Node(10)
    print("Here is the first node: ", first_node)

    first_csll = CSLL()
    for i in range(1, 6):
        first_csll.append(i * 10)
    print("Here is the appended CSLL")
    print(first_csll)

    print("Inserting -1000 at 0")
    first_csll.insert(-1000, 0)
    print(first_csll)
    print("Inserting -1000 at 5")
    first_csll.insert(-1000, 5)
    print(first_csll)
    print("Inserting -1000 at 4")
    first_csll.insert(-1000, 4)
    print(first_csll)

    print("Searching for -10: ", first_csll.search(-1))
    print("Searching for 10: ", first_csll.search(10))
    print("Searching for 50: ", first_csll.search(50))
    print("Searching for -1000: ", first_csll.search(-1000))

    print("\nTraversing the list using the get()")
    for i in range(first_csll.no_of_elements):
        print(f"Element: {i} -> ", first_csll.get(i))

    print("\nUpdating 0 to 0", first_csll.set(0, 0))
    print("Updating 7 to 7", first_csll.set(7, 7))
    print("Updated list:\n", first_csll)

    popped_ele = first_csll.pop()
    print("\nFirst popped element: ", popped_ele)
    popped_ele = first_csll.pop()
    print("Second popped element: ", popped_ele)
    print(first_csll)

    print("\nRemoving the 3rd element", first_csll.remove(3))
    print(first_csll)
    print("\nRemoving the 4th element", first_csll.remove(4))
    print(first_csll)

    first_csll.clear()
    print("Cleared CSLL\n", first_csll)

# ==== Driver Code ====
if __name__ == "__main__":
    main()
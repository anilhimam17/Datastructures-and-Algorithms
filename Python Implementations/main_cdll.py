from linear_structures.cdll import CDLL

# ==== The Main Function ====
def main():
    first_cdll = CDLL()
    print("Here is the default CDLL")
    print(first_cdll)

    for i in range(1, 6):
        first_cdll.append(i * 10)
    print("Here is the CDLL after appending the elements")
    print(first_cdll)

    print("Insert 0 at 0: ", first_cdll.insert(0, 0))
    print("Insert 6 at 6: ", first_cdll.insert(6, 6))
    print("Insert 100 at 2: ", first_cdll.insert(100, 2))
    print("Insert 100 at 6: ", first_cdll.insert(100, 6))
    print(first_cdll)

    print("\nSearching for 100: ", first_cdll.search(100))
    print("Searching for 6: ", first_cdll.search(6))
    print("Searching for 0: ", first_cdll.search(0))
    print("Searching for 64: ", first_cdll.search(64))

    print("\nTraversing the list using the get()")
    for i in range(first_cdll.no_of_elements):
        print(f"Element - {i}: ", first_cdll.get(i))
    
    print("\nUpdating 0 for 100: ", first_cdll.set(100, 0))
    print("Updating 8 for 6: ", first_cdll.set(6, 8))
    print("Updating 7 for 66: ", first_cdll.set(66, 7))
    print("Updating 3 for 44: ", first_cdll.set(44, 3))
    print(first_cdll)

    print("\nPopped element: ", first_cdll.pop())
    print("Popped element: ", first_cdll.pop())
    print(first_cdll)

    print("\nRemoving 0: ", first_cdll.remove(0))
    print("Removing 6: ", first_cdll.remove(5))
    print("Removing 4: ", first_cdll.remove(4))
    print("Removing 2: ", first_cdll.remove(2))
    print(first_cdll)

    print("Clearning the list.")
    first_cdll.clear()
    print(first_cdll)

# ==== Driver Code ====
if __name__ == "__main__":
    main()
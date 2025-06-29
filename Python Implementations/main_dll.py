from linear_structures.dll import DLL

# ==== Main Function ====
def main() -> None:
    print("Here is the first DLL.")
    first_dll = DLL()
    for i in range(1, 6):
        first_dll.append(i * 10)
    print(first_dll)

    print("Inserting 0 at 0: ", first_dll.insert(0, 0))
    print("Inserting 6 at 6: ", first_dll.insert(6, 6))
    print("Inserting -1000 at 6: ", first_dll.insert(-1000, 6))
    print("Inserting 400 at 4: ", first_dll.insert(400, 4))
    print(first_dll)

    print("Searching for -1000: ", first_dll.search(-1000))
    print("Searching for -2000: ", first_dll.search(-2000))
    print("Searching for 1: ", first_dll.search(1))
    print("Searching for 6: ", first_dll.search(6))

    print("\nTraversing the list using get")
    for i in range(first_dll.no_of_elements):
        print(f"Element - {i}: ", first_dll.get(i))

    print("\nUpdating -10 at 0: ", first_dll.set(-10, 0))
    print("Updating -6 at 8: ", first_dll.set(-6, 8))
    print("Updating -1000 at 3: ", first_dll.insert(-1000, 3))
    print(first_dll)

    print("Popped Element: ", first_dll.pop())
    print("Popped Element: ", first_dll.pop())
    print(first_dll)

    print("\nRemove element 3")
    first_dll.remove(3)
    print("\nRemove element 0")
    first_dll.remove(0)
    print("\nRemove element 5")
    first_dll.remove(5)
    print(first_dll)

    print("\nClearing the list.")
    first_dll.clear()
    print(first_dll)
    
# ==== Driver Code ====
if __name__ == "__main__":
    main()
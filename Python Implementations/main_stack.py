from linear_structures.stack import Stack

# The main function
def main() -> None:
    first_stack = Stack()
    print("Here is the default stack")
    print(first_stack)

    for i in range(1, 6):
        first_stack.push(i * 10)
    print("The stack after appending 5 elements")
    print(first_stack)

    for _ in range(2):
        popped_elem = first_stack.pop()
        print("Popped Element: ", popped_elem)
        print("Current Peek of the Stack: ", first_stack.peek())
    print("The stack after removing the last entered two elements")
    print(first_stack)

    print("Check if the stack is empty: ", first_stack.is_empty())
    print("Clearing the stack")
    first_stack.delete()
    print(first_stack)
    

if __name__ == "__main__":
    main()
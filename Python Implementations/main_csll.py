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

# ==== Driver Code ====
if __name__ == "__main__":
    main()
from linear_structures.queue import Queue
from linear_structures.sll import Node

# ==== The Main Function ====
def main() -> None:
    first_queue: Queue = Queue()
    print(first_queue)

    print("Enqueing 5 new nodes into the queue.")
    for i in range(1, 6):
        first_queue.enqueue(i * 10)
    print(first_queue)

    print("Removing the first two nodes.")
    for i in range(1, 3):
        deque_element: Node = first_queue.dequeue()
        print("Dequeue Node: ", deque_element)
        print(first_queue)

    print("Enqueing 5 more new nodes into the queue.")
    for i in range(1, 6):
        first_queue.enqueue(i * 20)
    print(first_queue)

    print("Removing the two more nodes.")
    for i in range(1, 3):
        deque_element: Node = first_queue.dequeue()
        print("Dequeue Node: ", deque_element)
        print("Peek Node: ", first_queue.peek())
    print(first_queue)

    new_queue: Queue = Queue()
    print("Empty Status of Queue 1: ", first_queue.is_empty())
    print("Empty Status of Queue 2: ", new_queue.is_empty())

    print("Clearing the Queue.")
    first_queue.delete()
    print(first_queue)

# ==== Driver Code ====
if __name__ == "__main__":
    main()
#include "linear_structures/queue.h"

// ==== Helper Functions ====
Node* Queue::get_node(int index) {
    Node* cursor = head;
    for (int i = 0; i < index; i++) {
        cursor = cursor->get_next();
    }
    return cursor;
}

// ==== Standard Methods ====
Queue::~Queue() {
    // Destructor for deallocating all the DAM used for SLL nodes in the queue.
    Node* cursor = head;
    while (cursor != nullptr) {
        Node* next = cursor->get_next();
        delete cursor;
        cursor = next;
    }
}

std::ostream& operator<<(std::ostream& os, const Queue& print_queue) {
    // Overloaded Extraction operator to display the queue.
    
    // If the queue is empty.
    if (!print_queue.head) {
        os << "None <= Head\nNone <= Tail\n";
    }
    // If the queue is not empty.
    else {
        Node* cursor = print_queue.head;
        while (cursor) {
            if (cursor == print_queue.head) {
                os << cursor->get_value() << " <= Head" << std::endl;
            }
            else if (cursor == print_queue.tail) {
                os << cursor->get_value() << " <= Tail" << std::endl;
            }
            else {
                os << cursor->get_value() << std::endl;
            }
            cursor = cursor->get_next();
        }
    }
    return os;
}

// ==== Member Functions ====
void Queue::enqueue(int value) {
    // Enter a new element to the Queue.

    // DAM for a new global node that comprises the Queue.
    Node* new_node = new Node(value);

    // If the Queue is empty.
    if (head == nullptr) {
        head = new_node;
        tail = new_node;
    }
    // If the Queue is not empty.
    else {
        tail->set_next(new_node);
        tail = new_node;
    }

    // Updating the no of elements in teh queue.
    no_of_elements += 1;
}

int Queue::dequeue() {
    // Removes the first elements in the queue and returns it.

    if (!head) {
        throw std::out_of_range("The queue is empty and has no elements that can be removed.");
    }

    // If the queue has only one element left.
    Node* remove_node = nullptr;
    if (no_of_elements == 1) {
        remove_node = head;
        head = nullptr;
        tail = nullptr;
    }
    // If the queue has more than one element left.
    else {
        remove_node = head;
        head = remove_node->get_next();
    }

    // Updating the link of the remove node
    remove_node->set_next(nullptr);

    // Updating the no of elements
    no_of_elements -= 1;
    return remove_node->get_value();
}

int Queue::peek() const {
    // Returns the top most element in the Queue.
    if (!head) {
        throw std::out_of_range("There are no elements in the list for peek.");
    }
    return head->get_value();
}

bool Queue::is_empty() const {
    // Returns a boolean for if the Queue is empty.
    if (no_of_elements == 0)
        return true;
    return false;
}

void Queue::delete_queue() {
    // Delete the entire queue.
    Node* cursor = head;
    while (cursor) {
        Node* next = cursor->get_next();
        delete cursor;
        cursor = next;
    }

    // Resetting the Pointers and Counter
    no_of_elements = 0;
    head = nullptr;
    tail = nullptr;
}
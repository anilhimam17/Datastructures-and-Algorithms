#include "sll.h"

// ==== Legacy ====
// Constructor
SLL::SLL() {}

// Destructor
SLL::~SLL() {
    // Deallocating the storage for all the nodes.
    Node* current = head;
    while(current != nullptr) {
        Node* next = current->get_next();
        delete current;
        current = next;
    }

    // Setting all the other instance variables to default.
    head = nullptr;
    tail = nullptr;
    no_of_elements = 0;
}

// ==== Helper functions ====
void SLL::append(int value) {
    // Adds a node to the end of the list.
    Node* new_node = new Node{value};

    // If the list is empty.
    if (head == nullptr) {
        head = new_node;
        tail = new_node;
    } 
    // If the list is not empty.
    else {
        // Updating the links.
        tail->set_next(new_node);
        tail = new_node;
    }

    // Updating the no of elements in the list.
    no_of_elements += 1;
}

void SLL::display() {
    // Displays all the current elements present in the list.
    if (head == nullptr) {
        std::cout << "None <= Head" << std::endl;
        std::cout << "None <= Tail" << std::endl;
    }
    else {
        Node* cursor = head;
        while(cursor != nullptr) {
            if (cursor == head) {
                std::cout << *cursor << " <= Head" << std::endl;
            } else if (cursor == tail) {
                std::cout << *cursor << " <= Tail" << std::endl;
            } else {
                std::cout << *cursor << std::endl;
            }

            // Updating the next_ptr for forward pass
            cursor = cursor->get_next();
        }
    }
}
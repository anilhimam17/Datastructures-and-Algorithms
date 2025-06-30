#include "linear_structures/csll.h"

// ==== Helper Function ====
void CSLL::free_nodes() {
    if (!head) return;
    SharedNode* cursor = head;
    do {
        SharedNode* next_node = cursor->get_next();
        cursor->set_next(nullptr);
        delete cursor;
        cursor = next_node;
    } while (cursor && cursor != head);
}

// ==== Legacy ====

// Constructor
CSLL::CSLL() = default;

// Desctructor
CSLL::~CSLL() {
    // Deleting all the DAM nodes
    CSLL::free_nodes();

    // Resetting the pointers
    head = nullptr;
    tail = nullptr;
    no_of_elements = 0;
}

// ==== Private Non - Member Function ====
// Overloaded extraction operator to manage the display of the list.
std::ostream& operator<<(std::ostream& os, const CSLL& csll) {
    if (csll.no_of_elements != 0) {
        auto cursor = csll.head;
        while(cursor) {
            if (cursor == csll.head) {
                os << cursor->get_value() << " <= Head" << std::endl;
            }
            else if (cursor == csll.tail) {
                os << cursor->get_value() << " <= Tail" << std::endl;
                break;
            }
            else {
                os << cursor->get_value() << std::endl;
            }
            cursor = cursor->get_next();
        }
    } 
    else {
        os << "None <= Head" << std::endl;
        os << "None <= Tail" << std::endl;
    }

    return os;
}

void CSLL::append(int value) {
    // Adds a new node to the end of the list.
    auto new_node = new SharedNode(value);

    // If there are no elements present in the list.
    if (no_of_elements == 0) {
        head = new_node;
        tail = new_node;
        new_node->set_next(new_node);
    }
    // If there are elements present in the list.
    else {
        tail->set_next(new_node);
        tail = new_node;
        new_node->set_next(head);
    }
    // Updating the no of elements in the list.
    no_of_elements += 1;
}

void CSLL::insert(int value, int index) {
    // Adds a new node at a given index in the list.
    // Bounds Check
    if ((index < 0) || (index > no_of_elements)) {
        throw std::out_of_range("The requested index is out of range.");
    }
    else {
        auto new_node = new SharedNode(value);

        // Inserting element at the start of the list
        if (index == 0) {
            new_node->set_next(head);
            head = new_node;
            tail->set_next(new_node);
        }
        // Inserting the element at the end of the list
        else if (index == no_of_elements) {
            CSLL::append(value);
        }
        // Inserting the element at any random location
        else {
            auto cursor = head;
            for (int i = 0; i < index - 1; i++) {
                cursor = cursor->get_next();
            }
            new_node->set_next(cursor->get_next());
            cursor->set_next(new_node);
        }
        // Updating the no of elements in the list.
        no_of_elements += 1;
    }
}

int CSLL::search(int value) {
    // Searches for a given value in the list and returns the index of the first find.
    if (!head) {
        return -1;
    }
    auto cursor = head;
    int i = 0;
    while(true) {
        // If hit then returns the index
        if (cursor->get_value() == value) {
            return i;
        }
        if (cursor == tail) {
            break;
        }
        // Updates the loop control variables
        cursor = cursor->get_next();
        i += 1;
    }
    // If loop completes then no hit returns -1
    return -1;
}

SharedNode* CSLL::get(int index) {
    // Returns a reference to the node requested
    // Bounds Check
    if ((index < 0) || (index >= no_of_elements)) {
        throw std::out_of_range("The requested index is out of range.");
    }
    // Traversing to the requested index
    auto cursor = head;
    for (int i = 0; i < index; i++) {
        cursor = cursor->get_next();
    }
    return cursor;
}

void CSLL::set(int value, int index) {
    // Updates the value of a given node identified by its index.
    auto update_node = CSLL::get(index);
    update_node->set_value(value);
}

SharedNode* CSLL::pop() {
    // Removes and returns the last node of the list.
    if (!head) {
        throw std::out_of_range("The list is empty no more nodes can be popped.");
    }
    SharedNode* popped_node = nullptr;
    if (no_of_elements == 1) {
        popped_node = head;
        head = nullptr;
        tail = nullptr;
    }
    else {
        auto previous_ele = CSLL::get(no_of_elements - 2);
        popped_node = tail;
        previous_ele->set_next(head);
        tail = previous_ele;
    }
    // Update the no of elements
    no_of_elements -= 1;
    popped_node->set_next(nullptr);
    return popped_node;
}

void CSLL::remove(int index) {
    // Removes the node identified by its index.
    if ((index < 0) || (index >= no_of_elements)) {
        throw std::out_of_range("The requested index is out of bounds.");
    }
    else {
        SharedNode* remove_node = nullptr;

        // If the node to be removed is the first node.
        if (index == 0) {
            remove_node = head;
            SharedNode* next_node = head->get_next();
            tail->set_next(next_node);
            head = next_node;
        }
        // If the node to be removed is the last node.
        else if (index == no_of_elements - 1) {
            CSLL::pop();
            return;
        }
        // Removing any random node in the middle.
        else {
            remove_node = CSLL::get(index);
            SharedNode* previous_node = CSLL::get(index - 1);
            previous_node->set_next(remove_node->get_next());
        }

        // Updating the links of the remove node
        remove_node->set_next(nullptr);

        // Updating the no of elements in the list.
        no_of_elements -= 1;
    }
}

void CSLL::clear() {
    // Clears all the elements in the list.
    CSLL::free_nodes();
    head = nullptr;
    tail = nullptr;
    no_of_elements = 0;
}


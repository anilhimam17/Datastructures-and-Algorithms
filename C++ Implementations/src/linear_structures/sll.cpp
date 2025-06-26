#include "linear_structures/sll.h"

// ==== Legacy ====
void SLL::free_nodes() {
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

// Constructor
SLL::SLL() {}

// Destructor
SLL::~SLL() {
    // Deallocating the storage for all the nodes.
    free_nodes();
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

void SLL::insert(int value, int index) {
    // Adds an elment at a given index.
    // Bounds check
    if ((index < 0) || (index > no_of_elements)) {
        std::cout << "Entered index is out of bounds" << std::endl;
    } else {
        Node* new_node = new Node(value);

        // Insert element at the start of the list.
        if (index == 0) {
            new_node->set_next(head);
            head = new_node;
        } 
        // Insert elements at the end of the list.
        else if (index == no_of_elements) {
            tail->set_next(new_node);
            tail = new_node;
        } 
        // Insert element at any random location in the list.
        else {
            // Traversing to the location to insert the element.
            Node* cursor = head;
            for (int i = 0; i < index - 1; i++) {
                cursor = cursor->get_next();
            }
            new_node->set_next(cursor->get_next());
            cursor->set_next(new_node);
        }
        // Updating the no of elements
        no_of_elements += 1;
    }
}

bool SLL::search(int value) {
    // Searches for a given value of the node and returns boolean on the first occurence.
    Node* cursor = head;
    while(cursor != nullptr) {
        if (cursor->get_value() == value) return true;
        else cursor = cursor->get_next();
    }
    return false;
}

int SLL::get_value(int index) const {
    // Access and returns the values of a node identified by its index.
    // Bounds check
    if ((index < 0) || (index >= no_of_elements)) {
        std::cout << "The requested index is out of bounds." << std::endl;
        return -1;
    }
    else {
        // If the first element is requested.
        if (index == 0) {
            return head->get_value();
        }
        // If the last element is requested.
        else if (index == no_of_elements - 1)
        {
            return tail->get_value();
        }
        // If any other random element is requested
        else {
            Node* cursor = head;
            for (int i = 0; i < index; i++) {
                cursor = cursor->get_next();
            }
            return cursor->get_value();
        }
    }
}

bool SLL::update(int value, int index) {
    // Updates the value of a node identified by its index.
    // If update is appl on the first node.
    if ((index < 0) || (index >= no_of_elements)) {
        std::cout << "The requested index is out of bounds." << std::endl;
        return false;
    }
    else {
        if (index == 0) {
            head->set_value(value);
        }
        // If update is appl on the last node.
        else if (index == no_of_elements - 1) {
            tail->set_value(value);
        }
        // If update is being applied on any random node.
        else {
            Node* cursor = head;
            for (int i = 0; i < index; i++) {
                cursor = cursor->get_next();
            }
            cursor->set_value(value);
        }
        return true;
    }
}

Node* SLL::pop() {
    // Removes and returns the very last element in the list.
    Node* popped_node = nullptr;

    // If there are no nodes remaining in the list.
    if (no_of_elements == 0) {
        std::cout << "There are no remaining nodes that can be popped." << std::endl;
        return nullptr;
    }
    // If there is only one node remaining in the list.
    else if (no_of_elements == 1) { 
        popped_node = head;
        head = nullptr;
        tail = nullptr;
    }
    // If there are more than one nodes remaining in the list.
    else {
        Node* cursor = head;
        for (int i = 0; i < no_of_elements - 2; i++) {
            cursor = cursor->get_next();
        }
        popped_node = cursor->get_next();
        cursor->set_next(nullptr);
        tail = cursor;
    }
    // Updating the number of elements
    no_of_elements -= 1;
    return popped_node;
}

void SLL::remove(int index) {
    // Removes any random node identified by its index.
    // Bounds check
    if ((index < 0) || (index >= no_of_elements)) {
        std::cout << "The requested element is out of bounds." << std::endl;
    } 
    else {
        Node* remove_ele = nullptr;
        // If element to be removed is at the start of the list.
        if (index == 0) {
            remove_ele = head;
            head = head->get_next();
        }
        // If element to be removed is at the end of the list.
        else if (index == no_of_elements - 1) {
            remove_ele = tail;
            Node* cursor = head;
            for (int i = 0; i < no_of_elements - 2; i++) {
                cursor = cursor->get_next();
            }
            tail = cursor;
        }
        // If the element to be removed is at a random index.
        else {
            Node* cursor = head;
            for (int i = 0; i < index - 1; i++) {
                cursor = cursor->get_next();
            }
            remove_ele = cursor->get_next();
            cursor->set_next(remove_ele->get_next());
        }
        // Setting the remove ele ptr to Null and updating the count
        remove_ele->set_next(nullptr);
        no_of_elements -= 1;
    }
}

void SLL::clear() {
    // Clears the list.
    if (no_of_elements == 0) {
        std::cout << "The list is already empty" << std::endl;
    }
    else {
        free_nodes();
    }
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
    std::cout << std::endl;
}
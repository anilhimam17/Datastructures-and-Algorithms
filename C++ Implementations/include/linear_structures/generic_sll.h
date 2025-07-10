#ifndef _GENERIC_SLL_H_
#define _GENERIC_SLL_H_

#include "generic_node.h"

template <class T>
class GenericSLL {
    // A structure that implements a Generic Singly Linked List styled Queue.
    private:
        GenericNode<T>* head;
        GenericNode<T>* tail;
        int no_of_elements;

        // ==== Overloaded Extraction Operator ====
        friend std::ostream& operator<<(std::ostream& os, const GenericSLL& generic_sll) {
            // If the list is empty.
            if (generic_sll.head == nullptr) {
                os << "None <= Head\nNone <= Tail";
            }
            // If the list is not empty.
            GenericNode<T>* cursor = generic_sll.head;
            while (cursor) {
                // Pretty printing each node
                if (cursor == generic_sll.head)
                    os << *cursor << " <= Head" << std::endl;
                else if (cursor == generic_sll.tail)
                    os << *cursor << " <= Tail" << std::endl;
                else
                    os << *cursor << std::endl;
                
                // Updating the loop control variable
                cursor = cursor->get_next();
            }

            // Returning the output stream
            return os;
        }
    public:
        // ==== Standard Methods ====
        GenericSLL<T>();
        ~GenericSLL<T>();

        // ==== Member Functions ====
        void append(GenericNode<T>* new_node);
        GenericNode<T>* remove();
};

// ==== Standard Methods ====
template <class T>
GenericSLL<T>::GenericSLL() 
: head{nullptr}, tail{nullptr}, no_of_elements{0} {};

template <class T>
GenericSLL<T>::~GenericSLL() {
    // If the list is not empty free up all the nodes.
    if (head != nullptr) {
        GenericNode<T>* cursor = head;
        while (cursor) {
            GenericNode<T>* next_node = cursor->get_next();
            delete cursor;
            cursor = next_node;
        }
    }

    // Reset the pointers for auto destructor.
    head = nullptr;
    tail = nullptr;
};

// ==== Member Functions ====
template <class T>
void GenericSLL<T>::append(GenericNode<T>* new_node) {
    // Adds a new elements to the end of the SLL.

    // If the list is empty
    if ((head == nullptr) && (no_of_elements == 0)) {
        head = new_node;
        tail = new_node;
    }
    // If the list is not empty
    else {
        tail->set_next(new_node);
        tail = new_node;
    }

    // Updating the no of elements
    no_of_elements += 1;
}

template <class T>
GenericNode<T>* GenericSLL<T>::remove() {
    // Removes the first elements of the list and returns it.
    if ((head == nullptr) || (no_of_elements == 0)) {
        throw std::out_of_range("The list is empty, add new elements before removal.");
    }

    // If the list has only one element left.
    GenericNode<T>* remove_node = head;
    if (no_of_elements == 1) {
        head = nullptr;
        tail = nullptr;
    }
    // Removing the node and updating the links
    else {
        head = head->get_next();
        remove_node->set_next(nullptr);
    }

    no_of_elements -= 1;
    return remove_node;
}

#endif
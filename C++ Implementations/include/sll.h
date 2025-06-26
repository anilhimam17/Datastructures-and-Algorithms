#include "node.h"
#ifndef _SLL_H_
#define _SLL_H_
class SLL {
    private:
        Node* head {nullptr};
        Node* tail {nullptr};
        int no_of_elements = 0;

        // ==== Helper function ====
        void free_nodes();
    public:
        // ==== Legacy ====
        // Constructor
        SLL();
        // Destructor
        ~SLL();

        // ==== Helper Functions ====
        // Adds an element to the end of the list.
        void append(int value);

        // Adds an element at a given index.
        void insert(int value, int index);

        // Searches for an element and returns a boolean for the first occurence.
        bool search(int value);

        // Access the value of a given node
        int get_value(int index) const;

        // Updates the values of a given node
        bool update(int value, int index);

        // Removes the very last node in the list.
        Node* pop();

        // Removes any random node identified by its index.
        void remove(int index);

        // Clears the list.
        void clear();

        // Displays all the current nodes present in the list. 
        void display();
};
#endif
#ifndef _CSLL_H_
#define _CSLL_H_

// Including the basic node class
#include "linear_structures/shared_node.h"

class CSLL {
    // Declare the blueprint for a generalised CSLL.
    private:
        // Instance Variables.
        SharedNode* head = nullptr;
        SharedNode* tail = nullptr;
        int no_of_elements = 0;

        // Private Non - Member Function.
        friend std::ostream& operator<<(std::ostream& os, const CSLL& csll);

    public:
        // ==== Legacy ====
        
        // Constructor
        CSLL();

        // Destructor
        ~CSLL();

        // ==== Helper Function ====
        void free_nodes();

        // ==== Member Functions ====

        // Adds a new node at the end of the list.
        void append(int value);

        // Inserts a new node at a given index of the list.
        void insert(int value, int index);

        // Searches for the first occurence of a node in the list and returns the index or -1.
        int search(int value);

        // Accesses a given node in the list identified by its index.
        SharedNode* get(int index);

        // Updates the value of a given node in the list identified by its index.
        void set(int value, int index);

        // Returns the current last node in the list.
        SharedNode* pop();

        // Removes a given node in the list identified by its index.
        void remove(int index);

        // Removes all the elements in the list.
        void clear();
};

#endif
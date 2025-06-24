#include "node.h"
#ifndef _SLL_H_
#define _SLL_H_
class SLL {
    private:
        Node* head {nullptr};
        Node* tail {nullptr};
        int no_of_elements = 0;
    public:
        // ==== Legacy ====
        // Constructor
        SLL();
        // Destructor
        ~SLL();

        // ==== Helper Functions ====
        // Adds an element to the end of the list.
        void append(int value);

        // Displays all the current nodes present in the list. 
        void display();
};
#endif
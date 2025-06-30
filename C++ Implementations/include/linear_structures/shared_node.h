#ifndef _SHARED_NODE_H_
#define _SHARED_NODE_H_

#include <iostream>
#include <sstream>

class SharedNode {
    private:
        // ==== Instance Variables ====
        int value = 0;
        SharedNode* next = nullptr;

        // ==== Private Non - Member Function ====
        friend std::ostream& operator<<(std::ostream& os, const SharedNode& node);

    public:
        // ==== Legacy ====
        // Constructor
        SharedNode(int value, SharedNode* next_ptr=nullptr);

        // Destructor
        ~SharedNode();
    
        // ==== Public Member Functions ====
        int get_value() const;
        SharedNode* get_next() const;

        void set_value(int value);
        void set_next(SharedNode* next);
};

#endif
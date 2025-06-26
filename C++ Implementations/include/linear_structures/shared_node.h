#ifndef _SHARED_NODE_H_
#define _SHARED_NODE_H_

#include <iostream>
#include <sstream>
#include <memory>

class SharedNode {
    private:
        // ==== Instance Variables ====
        int value = 0;
        std::shared_ptr<SharedNode> next = nullptr;

        // ==== Private Non - Member Function ====
        friend std::ostream& operator<<(std::ostream& os, const SharedNode& node);

    public:
        // ==== Legacy ====
        // Constructor
        SharedNode(int value, std::shared_ptr<SharedNode> next_ptr=nullptr);

        // Destructor
        ~SharedNode();
    
        // ==== Public Member Functions ====
        int get_value() const;
        std::shared_ptr<SharedNode> get_next() const;

        void set_value(int value);
        void set_next(std::shared_ptr<SharedNode> next);
};

#endif
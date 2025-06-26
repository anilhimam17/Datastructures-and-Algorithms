#ifndef _NODE_H_
#define _NODE_H_

#include <iostream>
#include <sstream>

class Node {
    private:
        int value {};
        Node* next_ptr {};
    public:
        // ==== Legacy ====
        // Constructors
        Node(int value, Node* next_ptr=nullptr);

        // Destructor
        ~Node();

        // ==== Getters and Setters
        Node* get_next() const;
        int get_value() const;
        void set_next(Node* next_node);
        void set_value(int value);

        // ==== Helper functions ====
        // String repr using Output Stream
        friend std::ostream& operator<<(std::ostream &os, const Node &node);

        // Overloaded assignment op for comparing nodes
        bool operator==(const Node &rhs) const;
};

#endif

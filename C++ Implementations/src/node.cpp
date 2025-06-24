#include "node.h"

// ==== Legacy ====
// Constructor
Node::Node(int value, Node* next_ptr) 
: value{value}, next_ptr{next_ptr} {};

// Destructor
Node::~Node() {
    next_ptr = nullptr;
}

// ==== Getters and Setters
Node* Node::get_next() const {
    return next_ptr;
}
void Node::set_next(Node* next_node) {
    next_ptr = next_node;
}

// ==== Helper functions ====
// Overloaded output stream operator
std::ostream& operator<<(std::ostream &os, const Node &node) {
    std::ostringstream oss {};
    oss << "Node(value=" << node.value << ", next=" << node.next_ptr << ")";
    os << oss.str();
    return os;
}

// Overloaded assignment op for comparing nodes
bool Node::operator==(const Node &rhs) const {
    if ((this->value == rhs.value) && this->next_ptr == rhs.next_ptr) return true;
    else return false;
}
#include "linear_structures/shared_node.h"

// ==== Legacy ====
// Constructor
SharedNode::SharedNode(int value, SharedNode* next_ptr)
: value{value}, next{next_ptr} {}

// Destructor
SharedNode::~SharedNode() = default;

// ==== Private Non - Member Function ====
std::ostream& operator<<(std::ostream& os, const SharedNode& node) {
    std::ostringstream oss;
    oss << "Node(value=" << node.value << ", next=" << node.next << ")" << std::endl;
    os << oss.str();
    return os;
}

// ==== Public Member Functions ====
int SharedNode::get_value() const {
    return value;
}

SharedNode* SharedNode::get_next() const {
    return next;
}

void SharedNode::set_value(int value) {
    this->value = value;
}
void SharedNode::set_next(SharedNode* next_node) {
    this->next = next_node;
}

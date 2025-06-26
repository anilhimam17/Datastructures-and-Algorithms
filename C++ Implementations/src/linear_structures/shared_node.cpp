#include "linear_structures/shared_node.h"

// ==== Legacy ====
// Constructor
SharedNode::SharedNode(int value, std::shared_ptr<SharedNode> next_ptr=nullptr)
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

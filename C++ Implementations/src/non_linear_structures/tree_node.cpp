#include "non_linear_structures/tree_node.h"

// ==== Standard Methods ====
// Constructor
TreeNode::TreeNode(int value) 
: value{value}, left_child{nullptr}, right_child{nullptr} {};

// Destructor
TreeNode::~TreeNode() {
    left_child = nullptr;
    right_child = nullptr;
    value = 0;
}

// Overloaded Extraction Operator
std::ostream& operator<<(std::ostream& os, const TreeNode& node) {
    os << "TreeNode(" << node.value << ")";
    return os;
}

// ==== Getters ====
int TreeNode::get_value() const {
    return this->value;
}

TreeNode* TreeNode::get_left_child() const {
    return this->left_child;
}

TreeNode* TreeNode::get_right_child() const {
    return this->right_child;
}

// ==== Setters ====
void TreeNode::set_value(int value) {
    this->value = value;
}

void TreeNode::set_left_child(TreeNode* node) {
    this->left_child = node;
}

void TreeNode::set_right_child(TreeNode* node) {
    this->right_child = node;
}
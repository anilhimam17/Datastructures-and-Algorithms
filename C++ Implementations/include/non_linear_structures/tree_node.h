#include <iostream>

class TreeNode {
    // Implements the node structure that will be used by the Binary Tree.
    private:
        int value;
        TreeNode* left_child;
        TreeNode* right_child;

        // Overloaded Extraction Operator
        friend std::ostream& operator<<(std::ostream& os, const TreeNode& node);

    public:
        // ==== Standard Methods ====
        TreeNode(int value);
        ~TreeNode();

        // ==== Getters ====
        int get_value() const;
        TreeNode* get_left_child() const;
        TreeNode* get_right_child() const;

        // ==== Setters ====
        void set_value(int value);
        void set_left_child(TreeNode* node);
        void set_right_child(TreeNode* node);
};
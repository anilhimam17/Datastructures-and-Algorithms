#include "linear_structures/generic_sll.h"
#include "non_linear_structures/tree_node.h"
using namespace std;

int main(int argc, char const *argv[])
{
    TreeNode new_tree_node {10};
    cout << "Here is the tree node: " << new_tree_node;

    GenericSLL<TreeNode> sll_of_tree_node = GenericSLL<TreeNode>();
    cout << "Appending 5 new nodes the SLL polymorphed with TreeNodes." << endl;
    for (int i = 1; i < 6; i++) {
        sll_of_tree_node.append(new GenericNode<TreeNode>(i * 10));
    }
    cout << sll_of_tree_node << endl;

    cout << "Removing the first 3 nodes." << endl;
    for (int i = 1; i < 4; i++) {
        GenericNode<TreeNode>* removed_node = sll_of_tree_node.remove();
        cout << "Removed Node: " << *removed_node << endl;

        // Deallocating the removed nodes
        delete removed_node;
    }
    cout << sll_of_tree_node << endl;

    cout << "Appending 5 more new nodes." << endl;
    for (int i = 1; i < 6; i++) {
        sll_of_tree_node.append(new GenericNode<TreeNode>(i * 100));
    }
    cout << sll_of_tree_node << endl;

    return 0;
}

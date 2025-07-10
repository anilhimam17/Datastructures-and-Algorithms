#include "generic_node.h"
#include "linear_structures/node.h"
using namespace std;

int main(int argc, char const *argv[])
{
    GenericNode<int> first_int_node {10};
    cout << first_int_node;

    GenericNode<Node> first_node_node {10};
    cout << first_node_node;
    
    return 0;
}

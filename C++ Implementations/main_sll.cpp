#include "node.h"
#include "sll.h"
using namespace std;

int main(int argc, char const *argv[])
{
    // Creating the first node
    Node first_node {10};
    cout << "Here is the first node: " << first_node << endl;

    // Creating the first Linked List
    SLL first_sll {};
    cout << "Here is the empty list" << endl;
    first_sll.display();
    
    cout << "Here is the list after appending 10" << endl;
    first_sll.append(10);
    first_sll.display();

    cout << "Here is the list after appending 20" << endl;
    first_sll.append(20);
    first_sll.display();

    cout << "Here is the list after appending 30" << endl;
    first_sll.append(30);
    first_sll.display();

    return 0;
}

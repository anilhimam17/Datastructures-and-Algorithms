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

    cout << "Here is the list after inserting -665 at 2" << endl;
    first_sll.insert(-665, 2);
    first_sll.insert(-1220, 4);
    first_sll.insert(-2240, 0);
    first_sll.display();

    bool flag1 = first_sll.search(-1220);
    bool flag2 = first_sll.search(-10);
    cout << "Search for -1220: " << flag1 << endl;
    cout << "Search for -10: " << flag2 << endl;
    cout << endl;

    cout << "Value at index - 10: " << first_sll.get_value(-10) << endl;
    cout << "Value at index - 3: " << first_sll.get_value(3) << endl;
    first_sll.display();

    cout << "Updating the value of 2 to -1000000" << endl;
    first_sll.update(-100000, 2);
    first_sll.update(-100000, 0);
    first_sll.update(-100000, 5);
    first_sll.display();

    Node* popped_elem = first_sll.pop();
    cout << "Popping the last current last element: " << *popped_elem << endl;
    first_sll.display();

    cout << "Removing the 0th element" << endl;
    first_sll.remove(0);
    first_sll.display();
    cout << "Removing the 2nd element" << endl;
    first_sll.remove(2);
    first_sll.display();

    cout << "Clearing the list." << endl;
    first_sll.clear();
    first_sll.display();

    return 0;
}

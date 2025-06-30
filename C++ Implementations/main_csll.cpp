#include <iostream>
#include "include/linear_structures/shared_node.h"
#include "include/linear_structures/csll.h"
using namespace std;

int main(int argc, char const *argv[])
{
    SharedNode first_shared_node {10};
    cout << "Here is the first shared node: " << first_shared_node << endl;

    CSLL first_csll {CSLL{}};
    first_csll.append(10);
    first_csll.append(20);
    first_csll.append(30);
    cout << "Here is the first of the CSLL" << endl;
    cout << first_csll << endl;

    first_csll.insert(-664, 0);
    cout << "Here is the CSLL after inserting -644" << endl;
    cout << first_csll << endl;
    first_csll.insert(-1228, 3);
    cout << "Here is the CSLL after inserting -1228" << endl;
    cout << first_csll << endl;

    int flag1 = first_csll.search(20);
    int flag2 = first_csll.search(-1000);
    cout << "First Search result -> " << flag1 << endl;
    cout << "Second Search result -> " << flag2 << endl;
    cout << endl;

    cout << "Displaying the elements using get:" << endl;
    for (int i = 0; i < 3; i++) {
        SharedNode node = *first_csll.get(i);
        cout << "Here is the " << i << "th node: " << node << endl;
    }

    cout << "Updating 0 to -1000" << endl;
    first_csll.set(-1000, 0);
    cout << first_csll << endl;
    cout << "Updating 4 to -1000" << endl;
    first_csll.set(-1000, 4);
    cout << first_csll << endl;

    cout << "Popping the last element: " << *first_csll.pop() << endl;
    cout << first_csll << endl;

    cout << "Appending 5 elements" << endl;
    for (int i = 1; i < 6; i++) {
        first_csll.append(i * 10);
    }
    cout << "Removing the 0th element" << endl;
    first_csll.remove(0);
    cout << first_csll << endl;
    cout << "Removing the 7th element" << endl;
    first_csll.remove(7);
    cout << first_csll << endl;
    cout << "Removing the 5th element" << endl;
    first_csll.remove(5);
    cout << first_csll << endl;
    cout << "Removing the 3rd element" << endl;
    first_csll.remove(3);
    cout << first_csll << endl;

    // cout << "Clearing the list." << endl;
    // first_csll.clear();
    // cout << first_csll << endl;

    return 0;
}

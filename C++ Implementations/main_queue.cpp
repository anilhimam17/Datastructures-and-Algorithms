#include "linear_structures/queue.h"
using namespace std;

int main(int argc, char const *argv[])
{
    Queue first_queue = Queue();
    cout << "Here is the default Queue" << endl;
    cout << first_queue;

    // Adding 10 new elements into the queue.
    cout << "Adding 10 new elements into the queue." << endl;
    for (int i = 1; i < 11; i++) {
        first_queue.enqueue(i);
    }
    cout << first_queue;

    // Removing 5 elements from the queue.
    cout << "Removing 5 elements from the queue" << endl;
    for (int i = 1; i < 5; i++) {
        cout << "Removed Element: " << first_queue.dequeue() << endl;
    }
    cout << first_queue;

    // Adding 10 new elements into the queue.
    cout << "Adding 10 new elements into the queue." << endl;
    for (int i = 1; i < 11; i++) {
        first_queue.enqueue(i * 10);
    }
    cout << first_queue;

    // Peek.
    cout << "Current Topmost Element: " << first_queue.peek() << endl;
    first_queue.dequeue();
    cout << "New Topmost Element: " << first_queue.peek() << endl;

    // Empty and Delete Ops.
    cout << "Checking for the queue to be empty " << first_queue.is_empty() << endl;
    cout << "Deleting the Queue" << endl;
    first_queue.delete_queue();
    cout << "Check for the queue to be empty " << first_queue.is_empty() << endl;
    
    return 0;
}

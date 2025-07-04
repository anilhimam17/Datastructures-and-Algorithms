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
    return 0;
}

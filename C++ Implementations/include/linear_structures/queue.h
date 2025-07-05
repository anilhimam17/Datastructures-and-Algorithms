#ifndef _QUEUE_H_
#define _QUEUE_H_ 

// ==== Standard Library ====
#include "linear_structures/node.h"

class Queue{
    private:
        Node* head = nullptr;
        Node* tail = nullptr;
        int no_of_elements = 0;
        friend std::ostream& operator<<(std::ostream& os, const Queue& print_queue);
    public:
        // ==== Standard Methods ====
        Queue() = default;
        ~Queue();

        // ==== Member Functions ====
        void enqueue(int value);
        int dequeue();
        int peek() const;
        bool is_empty() const;
        void delete_queue();

        // Helper functions
        Node* get_node(int index);
};

#endif
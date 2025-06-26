#include "linear_structures/csll.h"

// ==== Legacy ====

// Constructor
CSLL::CSLL() = default;

// Desctructor
CSLL::~CSLL() {
    head = nullptr;
    tail = nullptr;
    no_of_elements = 0;
}

// ==== Private Non - Member Function ====
std::ostream operator<<(std::ostream& os, const CSLL& csll) {
    // Overloaded extraction operator to manage the display of the list.
    if (csll.no_of_elements != 0) {
        auto cursor = csll.head;
        while(cursor) {
            if (cursor == csll.head) {
                os << cursor.get()->get_value() << " <= Head" << std::endl;
            }
            else if (cursor == csll.tail) {
                os << cursor.get()->get_value() << " <= Tail" << std::endl;
            }
            else {
                os << cursor.get()->get_value() << std::endl;
            }
            cursor = cursor.get()->get_next();
        }
    }
}
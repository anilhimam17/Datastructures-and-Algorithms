#ifndef _GENERIC_NODE_H_
#define _GENERIC_NODE_H_

#include <iostream>

template <class T>
class GenericNode {
    /* 
    Implements a generic node that can be polymorphed at compile time to hold different types of values.
    The types that can be held include primitive types and custom types.
    */
    private:
        // ==== Properties of the Class ====
        T value;
        GenericNode* next;

        // ==== Overloaded Extraction Operator ====
        friend std::ostream& operator<<(std::ostream& os, const GenericNode<T>& node) {
            os << "GenericNode(value=" << node.get_value() << ")";
            return os;
        }

        // ==== Overloaded Assignment Operator ====
        bool operator==(const GenericNode<T>& rhs) const;

    public:
        // ==== Standard Methods ====
        GenericNode(T value);
        ~GenericNode();

        // ==== Getters and Setters ====
        T get_value() const;
        GenericNode* get_next() const;

        void set_value(T value);
        void set_next(GenericNode<T>* next_node);
};


// ==== Implementation of the Functions ====
// ==== Standard Methods ====
template <class T>
GenericNode<T>::GenericNode(T value)
: value{value}, next{nullptr} {};

template <class T>
GenericNode<T>::~GenericNode() {
    next = nullptr;
}

// ==== Overloads ====
template <class T>
bool GenericNode<T>::operator==(const GenericNode<T>& rhs) const {
    return this->get_value() == rhs.get_value();
}

// ==== Getters and Setters ====
template <class T>
T GenericNode<T>::get_value() const {
    return this->value;
}

template <class T>
GenericNode<T>* GenericNode<T>::get_next() const {
    return this->next;
}

template <class T>
void GenericNode<T>::set_value(T value) {
    this->value = value;
}

template <class T>
void GenericNode<T>::set_next(GenericNode<T>* next_node) {
    this->next = next_node;
}

#endif
'''
 Implementation of Stack in python using Linked List

    Operations: append, pop, peek, isEmpty

    With their respective time and space complexity

    Can't wait to review the code with you

'''
#Creates a class that creates a node in the linked list
class Node:
    def __init__(self, data, ref=None):
        #Sets the data and the ref to the parameter passed to the Node class
        self.data = data
        self.ref = ref

        
#Creates a class that creates the linked list stack
class Stack:
    def __init__(self):
        #Sets the head of the linked list to None durimg instantiation
        self.head = None

    #Creates a method that adds an item to the end of the stack
    #Time complexity O(1) Constant time
    def append(self, item):
        #Creates a new node
        newNode = Node(item)
        #Sets the ref of the newly created head to the previous head, if the first node then the ref is set to none
        newNode.ref = self.head
        #Sets the newNode as the head of the linked list
        self.head = newNode


def main():
    stack = Stack()

    #Adds an item to the end of the stack
    stack.append(3)


if __name__ == '__main__':
    main()
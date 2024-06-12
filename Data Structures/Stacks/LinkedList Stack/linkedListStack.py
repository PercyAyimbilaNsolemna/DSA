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
        self._data = data
        self._ref = ref

        
#Creates a class that creates the linked list stack
class Stack:
    def __init__(self):
        #Sets the head of the linked list to None durimg instantiation
        self._head = None
        #Sets the size of the stack to zero
        self._size = 0

    #Creates a method that adds an item to the end of the stack
    #Time complexity O(1) Constant time
    def push(self, item):
        #Creates a new node
        newNode = Node(item)
        #Sets the ref of the newly created head to the previous head, if the first node then the ref is set to none
        newNode._ref = self._head
        #Sets the newNode as the head of the linked list
        self._head = newNode
        #Adds one to the size of the stack
        self._size += 1
        return

    #Creates a method that remmoves an element from the end of a stack
    #Time complexity O(1) Constant time
    def pop(self):
        #Checks if the stack is not empty
        if self._size == 0:
            raise Exception('The stack is EMPTY')
        
        #Sets the head of the stack to the ref of the current stack
        self._head = self._head._ref

        #Decrease the size of the stack by 1
        self._size -= 1
        return
    
    #Creates a method that outputs the top of the stack
    #Time complexity O(1) Constant time
    def peek(self):
        #Checks if the stack is empty
        if self._size == 0:
            print('The stack is EMPTY!')
            return 
        print(self._head._data)

    #Creates a method that checks if the stack is empty
    #Time complexity O(1) Constant Time
    def isEmpty(self):
        #Checks if the size of the stack is 0
        if self._size == 0:
            print(True)
            return
        
        #Outputs False if the stack has got elements
        print(False)
        return
    
    #Creates a method that outputs the size of the stack
    #Time complexity O(1) Constant Time
    def size(self):
        print(self._size)
        return
    
    #Creates a method that checkd if the stack contains a specified item
    #Time complexity O(N) Linear time. That is why stacks are not recommended for operations that requires searching
    def contains(self, item):
        #Checks if the stack is empty
        if self._size == 0:
            print('The stack is EMPTY!')
            return
        
        #Retrieves the head of the stack
        n = self._head

        #Loops through the elements in the stack
        while n is not None:
            #Checks if the element at that node is the same as the item
            if n._data == item:
                print(True)
                return
            n = n._ref

        print(False) 
        return

    #Creates a method that outputs all the elements in the stack
    def traverse(self):
        #Checks if the head of the linked list is empty then it outputs the linked list is empty
        if self._head is None:
            print('Linked List is empty')
            return
        else:
            #Pulls the head of the linked list
            n = self._head
            
            #Enters the loop if the head is not none and the folloowing nodes are having a ref to a different node 
            while n is not None:
                print(n._data, '===>', end=' ')
                #Sets the n to the ref of the next node
                n = n._ref
        print()
        return


def main():
    stack = Stack()

    #Adds an item to the end of the stack
    stack.push(3)
    stack.push(8)
    stack.push(10)
    stack.push(15)
    stack.push('Name')

    #Traverses the stack
    stack.traverse()
    #Removes an element from the end of the stack
    stack.pop()
    #Traverses the stack
    stack.traverse()
    #Outputs the size of the stack
    stack.size()
    #Outputs the last element in the stack
    stack.peek()
    #Checks if the stack is empty
    stack.isEmpty()
    #Checks if the stack contains
    stack.contains('Name')

    stack1 = Stack()
    stack1.pop()
    stack1.isEmpty()


if __name__ == '__main__':
    main()
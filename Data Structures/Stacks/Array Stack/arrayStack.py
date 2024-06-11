'''
    Implementation of Stack in python using Lists

    Operations: append, pop, peek, isEmpty

    With their respective time and space complexity

    Can't wait to review the code with you

'''

class Stack:
    #Method called when instantiating a stack class
    def __init__(self):
        self._stack = []
        #Creates a size property and set it to none when the Stack class is instantiated
        self._size = 0

    #Defines a __str__ methos that returns the stack if the stack object is called by the print function
    def __str__(self):
        #Returns the stack
        return str(self._stack)

    #Creates a method that adds an item to the stack
    #Time complexity O(1) constant time
    def append(self, item):
        #Adds one to the size of the stack anytime an item is added so we can keep track of the size of the stack
        self._size += 1
        #Adds item to the end of the stack
        self._stack.append(item)
        return self._stack
    
    #Creates a method that removes the last element from the array stack
    #Time complexity O(1) constant time 
    def pop(self):
        #Checks if the stack is empty
        if self._size == 0:
            raise Exception('Stack is EMPTY!')
        
        #Decreases the size of the stack by 1
        self._size -= 1

        #Removes the last element from the stack
        self._stack.pop()
        
        #Retruns
        return
    
    #Creates a method that shows the last element in the statck without removing it
    #Time complexity O(1) constant time
    def peek(self):
        #Checks if the stack is empty
        if self._size == 0:
            print('The stack is empty')

            return 
        
        #Prints the last element in the stack
        print(self._stack[self._size - 1])

        return
    
    #Creates a method that checks if the stack is empty
    #Time complexity O(1) constant time
    def isEmpty(self):
        #Checks if the stack is empty
        if self._size == 0:
            print(True)
            return

        #Outputs False if the stack is not empty and return
        print(False)
        return 

    #Creates a method that returns the size of the array
    #Time complexity O(1) constant time
    def size(self):
        #Outputs the size of the stack and returns 
        print(self._size)
        return

    #Creates a method that checks if an element is in  the stack
    #Time complexity O(N) Linear time. That is why Stacks are not recommended for tasks that requires searching
    def contains(self, element):
        #Checks if the stack is empty and returns False
        if self._size == 0:
            print(False)
            return
        
        #Loops through the elements in the stack and prints True if the element is found
        for item in self._stack:
            if item == element:
                print(True)
                return

        #Prints False and returns if the for loop runs through all the items and does not find the element
        print(False)    
        return

def main():
    #Creates an object from the Stack class
    stack = Stack()

    #Appends elements to the end of the stack
    print(stack.append(2))
    print(stack.append(5))
    print(stack.append(6))
    print(stack.append(1))
    print(stack.append(3))

    #Checks the size of the stack
    stack.size()

    #Removes an element from the end of the stack (LIFO)
    stack.pop()
    print(stack)

    #Gets the last element in the stack
    stack.peek()

    #Checks if the stack is empty
    stack.isEmpty()

    #Checks if the stack contains an element
    stack.contains(2)

    stack1 = Stack()
    stack1.peek()
    #Shoots an error since the stack is empty
    #stack1.pop()
    stack1.isEmpty()
    stack1.size()
    print(stack1)
    stack1.contains(3)
    

if __name__ == '__main__':
    main()
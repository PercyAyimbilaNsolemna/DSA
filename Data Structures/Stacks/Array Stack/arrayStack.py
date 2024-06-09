'''
    Implementation of Stack in python using Lists

    Operations: append, pop, peek, isEmpty

    With their respective time and space complexity

    Can't wait to review the code with you

'''

class Stack:
    #Method called when instantiating a stack class
    def __init__(self, stack=[], size=0):
        self.stack = stack
        #Creates a size property and set it to none when the Strack class is instantiated
        self.size = size

    #Creates a method that adds an item to the stack
    def append(self, item):
        #Adds one to the size of the stack anytime an item is added so we can keep track of the size of the stack
        self.size += 1
        #Adds item to the end of the stack
        self.stack.append(item)
        return self.stack
    
    #Creates a method that removes the last element from the array stack
    def pop(self):
        #Checks if the stack is empty
        if self.size == 0:
            raise Exception('Stack is EMPTY!')
        
        #Decreases the size of the stack by 1
        self.size -= 1

        #Removes the last element from the stack
        self.stack.pop()
        
        #Retruns
        return
    
    #Creates a method that shows the last element in the statck without removing it
    def peek(self):
        #Checks if the stack is empty
        if self.size == 0:
            print('The stack is empty')

            return 
        
        #Prints the last element in the stack
        print(self.stack[self.size - 1])

        return
    
    #Creates a method that checks if the stack is empty
    def isEmpty(self):
        #Checks if the stack is empty
        if self.size == 0:
            print(True)
            return

        #Outputs False if the stack is not empty and return
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
    print(stack.size)

    #Removes an element from the end of the stack (LIFO)
    stack.pop()
    print(stack.stack)

    #Gets the last element in the stack
    stack.peek()

    #Checks if the stack is empty
    stack.isEmpty()

    stack1 = Stack()
    stack1.peek()
    #Shoots an error since the stack is empty
    #stack1.pop()
    stack1.isEmpty()

if __name__ == '__main__':
    main()
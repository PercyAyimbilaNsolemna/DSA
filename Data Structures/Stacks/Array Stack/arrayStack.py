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

def main():
    stack = Stack()
    print(stack.append(2))
    print(stack.append(5))
    print(stack.append(6))
    print(stack.append(1))
    print(stack.append(3))
    print(stack.size)

if __name__ == '__main__':
    main()
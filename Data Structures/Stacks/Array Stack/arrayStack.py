'''
    Implementation of Stack in python using Lists

    Operations: append, pop, peek, isEmpty

    With their respective time and space complexity

    Can't wait to review the code with you

'''

class Stack:
    #Method called when instantiating a stack class
    def __init__(self, size=None):
        #Creates a size property and set it to none when the Strack class is instantiated
        self.size = size

def main():
    stack = Stack()
    print(stack.size)

if __name__ == '__main__':
    main()
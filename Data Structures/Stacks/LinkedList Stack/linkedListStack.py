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
        #Sets the size of the stack to zero
        self.size = 0

    #Creates a method that adds an item to the end of the stack
    #Time complexity O(1) Constant time
    def push(self, item):
        #Creates a new node
        newNode = Node(item)
        #Sets the ref of the newly created head to the previous head, if the first node then the ref is set to none
        newNode.ref = self.head
        #Sets the newNode as the head of the linked list
        self.head = newNode
        #Adds one to the size of the stack
        self.size += 1
        return

    #Creates a method that remmoves an element from the end of a stack
    #Time complexity O(1) Constant time
    def pop(self):
        #Checks if the stack is not empty
        if self.size == 0:
            print('The stack is EMPTY!')
            return
        #Sets the head of the stack to the ref of the current stack
        self.head = self.head.ref

        #Decrease the size of the stack by 1
        self.size -= 1
        return
    
    #Creates a method that outputs the top of the stack
    #Time complexity O(1) Constant time
    def peek(self):
        #Checks if the stack is empty
        if self.size == 0:
            print('The stack is EMPTY!')
            return 
        print(self.head.data)

    #Creates a method that outputs all the elements in the stack
    def traverse(self):
        #Checks if the head of the linked list is empty then it outputs the linked list is empty
        if self.head is None:
            print('Linked List is empty')
            return
        else:
            #Pulls the head of the linked list
            n = self.head
            
            #Enters the loop if the head is not none and the folloowing nodes are having a ref to a different node 
            while n is not None:
                print(n.data, '===>', end=' ')
                #Sets the n to the ref of the next node
                n = n.ref
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

    stack.traverse()

    print(stack.size)

    stack.peek()

    stack1 = Stack()
    stack1.pop()


if __name__ == '__main__':
    main()
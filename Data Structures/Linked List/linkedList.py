'''
    This is an implementation of linked list

    The operations that can be performed on the linked list are,

    Insertion, Iteration and Deletion

    Detailed explanation

'''
#Class that reates the Nodes
class Node:
    def __init__(self, data, ref=None):
        #Sets the data to the parameter passed
        self.data = data
        self.ref = ref

#Class that links the nodes crrated
class LinkedList:
    def __init__(self):
        #Sets the head to None during instantiation
        self.head = None
    
    #Loops through all the nodes in the linked list
    def traverse(self):
        #Checks if the head of the linked list is empty then it outputs the linked list is empty
        if self.head is None:
            print('Linked List is empty')
        else:
            #Pulls the head of the linked list
            n = self.head
            
            #Enters the loop if the head is not none and the folloowing nodes are having a ref to a different node 
            while n is not None:
                print(n.data, '===>', end=' ')
                #Sets the n to the ref of the next node
                n = n.ref
            print()
    #Adds a node to the beginning of the linked list
    def addItemAtBegining(self, data):
        #Creates a new node from the node class
        newNode = Node(data)
        #Sets the ref of the newly created node to the previous head, if the first node then the head is none so ref is none
        newNode.ref = self.head
        #Sets the head to the newly created node
        self.head = newNode

    #Adds a node to teh end of the linked list
    def addItemAtEnd(self, data):
        #Creates the new node
        newNode = Node(data)
        if self.head is None:
            #Sets the head to the new node since there isn't any available node
            self.head = newNode
        else:
            #Loops through the linked list to the end, since the ref of the last node will be none that condition is used
            n = self.head
            while n.ref is not None:
                n = n.ref

            #Sets the ref of the last node to the newly created node 
            n.ref = newNode

    #Method thyat inserts a node after a give node
    def insertAfter(self, node, data):

        #Loops through the nodes to find the node that has the requested data to insert the data after
        n = self.head
        while n is not None:
            #Checks if the data is the same as the node requested, if true saves the node and the next  node
            if n.data == node:
                foundNode = n
                break
            n = n.ref
        if n is None:
            print(f'The Node {node} is not present in the linked list!!')
        else:
            newNode = Node(data)
            #Sets the found node's ref to the new node 
            newNode.ref = n.ref
            #Sets the new node's ref to the node that was just after the found node 
            n.ref = newNode

    #Method that inserts a node before a specified node
    def insertBefore(self, node, data):
        #Exits the code if the linked list is empty
        if self.head  is None:
            print('The Linked List is Empty')
            return 
        
        #Handles inserting a node before the head
        if self.head.data == node:
            newNode = Node(data)
            newNode.ref = self.head
            self.head = newNode
            return
        
        #Handles inserting a node before any other node
        n = self.head

        while n.ref is not None:
            #Checks if the data in the next node is the same as the requested node. If found the loop construct is exited
            if n.ref.data == node:
                break
            n = n.ref

        #Exit the code if the requested node is not found
        if n.ref is None:
            print(f'The Node {node} is not in the Linked List')
            return 
        
        #Creates a new node
        newNode = Node(data)
        #Sets the new node's ref to the prev node of the requested node
        newNode.ref = n.ref
        #Sets the ref of the node to the new node
        n.ref = newNode

    #Method that removes a node from the linked list
    def remove(self, node):
        #Checks if the head is none and outputs the a message if the head is None
        if self.head is None:
            print('The linked list is empty!')
            return 
        
        #Checks if the data to remove is the head in the linked list
        if self.head.data == node:
            #If there is/are node(s) after the head node, the head becomes the node after the head node
            if self.head.ref is not None:
                self.head = self.head.ref
                return 
            #If there is/are no node(s) after the head node, the head node is set to None
            else:
                self.head = None
                return

        #Gets the head of the nodes in the linked list   
        n = self.head

        #Loops through the linked list and check if the data is equal to the requested data to remove
        while n is not None:
            #If the nest node of the current node is None that means we've gotten to the end of the linked list
            if n.ref is None:
                print(f'The node {node} is not in the Linked List')
                return 
            #Checks if the data of the next node of the current node is equal to the requested node to delete
            if n.ref.data == node:
                break
            #Sets the n value to the next node in the linked list
            n = n.ref
        
        #Sets the ref of the current node to the ref of the next node, this jumps the node to delete 
        n.ref = n.ref.ref

    #Method to remove a node after a specified node
    def removeAfter(self, node):
        #Gets the head of the linked list
        n = self.head

        #Loops through the nodes in the linked list in search of the requested node
        while n is not None:
            #Checks if the data at the node is the specified node
            if n.data == node:
                break
            
            #Sets the n value to the next node
            n = n.ref

        #Outputs a tyext when the requested node is not found in the linked list
        if n is None:
            print(f'The node {node} is not in the Linked List')
            return

        #Sets the ref of the current node to the next node of the following node, this jumps the next node
        n.ref = n.ref.ref


    #Method to delete a node before the speified node
    def removeBefore(self, node):
        #Checks if the specified node is the head node
        if self.head.data == node:
            print(f'{node} is the head node')
            return 
        
        #Checks if the node to remove is the head node
        if self.head.ref.data == node:
            self.head = self.head.ref
            return
        
        #Sets n to the head node
        n = self.head

        #Loops through the nodes to find the specified node
        while n is not None:
            #If the nest node of the current node is None that means we've gotten to the end of the linked list
            if n.ref.ref is None:
                print(f'The node {node} is not in the Linked List')
                return 
            
            #Checks the data in the next two nodes if is equal to the specified node
            if n.ref.ref.data == node:
                break
            
            #Updates the node to the next node
            n = n.ref

        #Changes the ref of the current node to the next two nodes
        n.ref = n.ref.ref


    #Method to print a specified node
    def printNode(self, node):
        #Sets n to the head node
        n = self.head

        #Loops through the nodes in the linked l;ist
        while n is not None:
            #Checks if the data at the node is equal to the specified node
            if n.data == node:
                print(node)
                return 
            
            n = n.ref

        #Outputs a message if the node is NOT found in the linked list
        print(f'{node} node is NOT in the Linked List')
        

    #Method to print node after a specified node
    def printNodeAfter(self, node):
        #Sets n to the head of the Linked List
        n = self.head

        #Loops through the linked List 
        while n is not None:
            if n.data == node:
                break

            n = n.ref

        #Checks if n is None
        if n is None:
            print(f'{node} node is NOT in the Linked List')
            return

        #Checks if the ref to the next node is None
        if n.ref is None:
            print(f'{node} node is the last node in the Linked List')
            return 
        
        #Prints the data in the next node
        print(n.ref.data)

    #Method to print node before a specified node
    def printNodeBefore(self, node):
        #Checks if the specified node is the head node
        if self.head.data == node:
            print(f'{node} is the head node, there is NO node before it')
            return
        
        #Sets n to the head node
        n = self.head

        #Loops through the Linked List
        while n is not None:
            #Checks if the ref of the next node is None
            if n.ref is None:
                print(f'{node} node is NOT in the Linked List')
                return
            #Checks if the data in the next node is equal to the specified node
            if n.ref.data == node:
                break
            
            #Sets n to the next node
            n = n.ref
      
        print(n.data)

    #Method that reverses a linked list
    def reverse(self, linkedList=None):
        '''
        2 ---> 3 ---> 4 --> 5
        prev: point to the node before current
        current: Point to the current node
        next: Pointing to the next node to the current
        '''
        #Sets the pointer of the previous node to the current node to None
        prev = None

        #Sets the pointer of the next node to the current node to None
        next = None

        #Sets the current node to the head node
        current = self.head

        #Checks if the head node is None
        if current is None:
            print('The linked list is empty')
            return 

        #Loops through the linked list
        while current is not None:
            #Sets the next node to the current node 
            next = current.ref
            
            #Sets the ref of the current node to the prev node
            current.ref = prev

            #Updates the prev node to the current node
            prev = current 

            #Updates the current node to the next node
            current = next

        #print(f'The data at the node is {prev.data}')
        #Sets the head node to the prev node, that is the last node with next node been None
        #The ref has already been set to the prev node hence no need to update the ref again
        self.head = prev
        return 


def main():
    
    linkedList = LinkedList()
    linkedList.addItemAtEnd('Kingdergarten')
    linkedList.addItemAtEnd('Primary')
    linkedList.addItemAtEnd('High school')
    linkedList.addItemAtBegining('University')
    linkedList.addItemAtEnd('Primary')
    linkedList.addItemAtEnd('High school')
    linkedList.addItemAtEnd('University')
    linkedList.addItemAtBegining('Kindergarten')
    linkedList.addItemAtEnd('Primary')
    linkedList.addItemAtEnd('High school')
    linkedList.addItemAtEnd('University')
    linkedList.traverse()
    print()
    print('-------------------------------------------------')
    print()
    linkedList.removeBefore('Kindergarten')
    linkedList.printNodeBefore('High school')
    linkedList.insertBefore('High school', 'JHS')
  

    '''

    linkedList.addItemAtBegining('Kingdergarten')
  
    linkedList.addItemAtBegining('Primary')
  
    linkedList.addItemAtBegining('Secondary')

    linkedList.addItemAtBegining('University')

    '''
    linkedList.traverse()
    
    linkedList.reverse()
    print()
    print('------------------------------------------------- Reverse')
    print()
    linkedList.traverse()
    


if __name__ == '__main__':
    main()
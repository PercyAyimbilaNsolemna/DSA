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

    def __str__(self):
        return 'Class for Node'

#Class that links the nodes crrated
class LinkedList:
    def __init__(self):
        #Sets the head to None during instantiation
        self.head = None

    def __str__(self):
        return 'Class for Linked List'
    
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
        

def main():
    
    linkedList = LinkedList()
    '''
    linkedList.addItemAtEnd('Kingdergarten')
    linkedList.addItemAtEnd('Primary')
    linkedList.addItemAtEnd('High school')
    linkedList.addItemAtBegining('University')
    '''
    linkedList.addItemAtBegining('Kindergarten')
    linkedList.addItemAtEnd('Primary')
    linkedList.addItemAtEnd('High school')
    linkedList.addItemAtEnd('University')
    linkedList.traverse()
    print()
    print('-------------------------------------------------')
    print()
    linkedList.insertBefore('High school', 'JHS')
  

    '''

    linkedList.addItemAtBegining('Kingdergarten')
  
    linkedList.addItemAtBegining('Primary')
  
    linkedList.addItemAtBegining('Secondary')

    linkedList.addItemAtBegining('University')

    '''
    linkedList.traverse()
    


if __name__ == '__main__':
    main()
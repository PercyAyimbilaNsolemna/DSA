''''
    Implementation of Queues in python using Linked List

    Operations: enqueue, dequeue, top, and size

    With their respective time and space complexity

    Be my guest

'''

#Creates a class node which will be used to create nodes in the linked lst
class Node():
    def __init__(self, data, ref=None):
        self._data = data
        self._ref = ref

#Creates a class to be used to create the queue
class Queue():
    def __init__(self):
        #Sets the head of the queue to none
        self._head = None
        #Sets the tail to none
        self._tail = None
        #Sets the size of the queue to zero
        self._size = 0


    #Creates a class that adds an element to the queue
    def enqueue(self, item):
        #Creates a new node
        newNode = Node(item)

        #Checks if the queue is empty
        if self._size == 0:
            #Sets the ref of the newNode to None
            newNode._ref = self._head
            #Sets the newNode as the head node
            self._head = newNode
            #Sets the newNode as the tail 
            self._tail = self._head
            self._size += 1
            return
        
        #If there is/are nodes in the queue
        #Creates a newNode
        newNode = Node(item)
        #Sets the ref of the last node in the queue to the new node added
        self._tail._ref = newNode
        #Sets the tail of the queue to the new node
        self._tail = newNode
        #Increment the size of the queue by 1
        self._size += 1
        return
    
    #Creates a method that removes the first item from the queue
    def dequeue(self):
        #Checks if the queue is empty
        if self._size == 0:
            raise Exception('The queue is EMPTY!')
        
        #Removes the first element from the queue by setting the head to the ref of the current head
        self._head = self._head._ref
        #Decreses the number of elements in the queue by one
        self._size -= 1

    #Creates a method that checks the size of the queue
    def size(self):
        if self._size == 0:
            print('The queue is EMPTY!')
            return
        
        print(self._size)
        return


    #Creates a traverse method that loops through the queue and outputs each node in the queue
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
    queue = Queue()

    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.size()
    queue.traverse()
    queue.dequeue()
    queue.traverse()


if __name__ == '__main__':
    main()
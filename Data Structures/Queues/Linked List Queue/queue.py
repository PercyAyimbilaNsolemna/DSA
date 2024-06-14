''''
    Implementation of Queues in python using Linked List

    Operations: enqueue, dequeue, top, and size

    With their respective time and space complexity

    Be my guest

'''

#Creates a class node which will be used to create nodes in the linked lst
class Node():
    def __init__(self, data, ref=None):
        self.data = data
        self.ref = ref

#Creates a class to be used to create the queue
class Queue():
    def __init__(self):
        #Sets the head of the queue to none
        self.head = None
        #Sets the tail to none
        self.tail = None
        #Sets the size of the queue to zero
        self.size = 0


    #Creates a class that adds an element to the queue
    def enqueue(self, item):
        #Creates a new node
        newNode = Node(item)

        #Checks if the queue is empty
        if self.size == 0:
            #Sets the ref of the newNode to None
            newNode.ref = self.head
            #Sets the newNode as the head node
            self.head = newNode
            #Sets the newNode as the tail 
            self.tail = self.head
            self.size += 1
            return
        
        #If there is/are nodes in the queue
        #Creates a newNode
        newNode = Node(item)
        #Sets the ref of the last node in the queue to the new node added
        self.tail.ref = newNode
        #Sets the tail of the queue to the new node
        self.tail = newNode
        #Increment the size of the queue by 1
        self.size += 1
        return

    #Creates a traverse method that loops through the queue and outputs each node in the queue
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
    queue = Queue()

    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    print(queue.size)
    queue.traverse()


if __name__ == '__main__':
    main()
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
            return

def main():
    ...


if __name__ == '__main__':
    main()
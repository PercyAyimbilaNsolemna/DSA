'''
    Implement the MyCircularQueue class:

    MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    int Front() Gets the front item from the queue. If the queue is empty, return -1.
    int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
    boolean isEmpty() Checks whether the circular queue is empty or not.
    boolean isFull() Checks whether the circular queue is full or not.

    Input
    ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
    [[3], [1], [2], [3], [4], [], [], [], [4], []]
    Output
    [null, true, true, true, false, 3, true, true, true, 4]

    Explanation
    MyCircularQueue myCircularQueue = new MyCircularQueue(3);
    myCircularQueue.enQueue(1); // return True
    myCircularQueue.enQueue(2); // return True
    myCircularQueue.enQueue(3); // return True
    myCircularQueue.enQueue(4); // return False
    myCircularQueue.Rear();     // return 3
    myCircularQueue.isFull();   // return True
    myCircularQueue.deQueue();  // return True
    myCircularQueue.enQueue(4); // return True
    myCircularQueue.Rear();     // return 4

    Constraints:

    1 <= k <= 1000
    0 <= value <= 1000
    At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull

'''

class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue_max_size = k
        #Sets the size of the array to store the queue to be the parameter passed when initializing the circular queue 
        self.size = 0
        #Sets the head of the queue to zero
        self.head = 0
        #Sets the tail of the queue to zero
        self.tail = 0
        #Sets the list
        self.queue = []
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.size == 0:
            #Adds the value to the end of the queue
            self.queue.append(value)
            #Adds one to the tail of the queue
            self.tail += 1
            #Adds one to the tail of the queue
            self.head += 1
            #Adds one to the size of the queue
            self.size += 1
            return True
        
        #Checks if the size is full
        elif self.tail == self.queue_max_size:
            #Checks if the first element is not None, that means there is an element at the first position
            if self.queue[0] is not None:
                return False
            #Set the value of the first position to the element passed to enQueue
            self.queue[0] = value
            self.tail = 1
            self.size += 1
            return True
       
        #Checks if the tail is less than or equal to the head
        elif self.tail < self.head:
            #Checks if the next position to add the element is the same as the head then it returns  False
            if self.tail+1 == self.head:
                return False
            if self.queue[self.tail+1] is not None:
                return False
            self.queue[self.tail+1] = value
            self.tail += 1
            self.size += 1
            return True
        
        else:
            #Adds the value to the queue
            self.queue.append(value)
            #Adds one to the tail
            self.tail += 1
            self.size += 1
            return True



    def deQueue(self):
        """
        :rtype: bool
        """
        #Checks if the tail is less than the head, that means the queue has rapped around
        if self.tail < self.head:
            if self.head == self.queue_max_size:
                if self.queue[0] is not None:
                    self.queue[self.head-1] = None
                    self.head = 1
                    self.size -= 1
                    return True
                else:
                    self.queue[self.head-1] = None
                    self.size = 0
                    self.head = 0
                    self.tail = 0
                    return True
            else:
                self.queue[self.head-1] = None
                self.head += 1
                self.size -= 1
                return True
        elif self.tail == self.head:
            self.queue[self.head-1] = None
            self.head = 0
            self.size = 0
            self.tail = 0
            return True
        else:
            self.queue[self.head-1] = None
            self.head += 1
            self.size -= 1
            return True
 

    def Front(self):
        """
        :rtype: int
        """
        #Subtracts 1 from the head because indexing starts from zero
        return self.queue[self.head-1]

    def Rear(self):
        """
        :rtype: int
        """
        #Subtracts 1 from the tail beacuse indexing starts from zero
        return self.queue[self.tail-1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        #Returns true if the head is zero
        if self.head != 0:
            return True
        #Returns False if the head is not zero
        return False

    def isFull(self):
        """
        :rtype: bool
        """
        if self.size == self.queue_max_size:
            return True
        return False
    
    def printQueue(self):
        return self.queue
        
def main():
    myCircularQueue = MyCircularQueue(3)

    
    print(myCircularQueue.enQueue(1)) # return True
    print(myCircularQueue.enQueue(2))  #return True
    print(myCircularQueue.enQueue(3))  #return True
    #print(myCircularQueue.printQueue())
    print(myCircularQueue.enQueue(4)) #return False
    print(myCircularQueue.Rear())     #return 3
    print(myCircularQueue.isFull())   #return True
    print(myCircularQueue.deQueue())  #return True
    #print(myCircularQueue.printQueue())
    print(myCircularQueue.enQueue(4)) #return True
    print(myCircularQueue.printQueue())
    print(myCircularQueue.Rear())     #return 4


if __name__ == '__main__':
    main()
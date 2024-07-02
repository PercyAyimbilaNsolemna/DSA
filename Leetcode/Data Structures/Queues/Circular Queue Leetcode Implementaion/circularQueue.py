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

    Implement an improved version of the previous implementation

    Remove the explicit for loop when initializing the queue, for the code to run faster

'''

class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """

    def deQueue(self):
        """
        :rtype: bool
        """

    def Front(self):
        """
        :rtype: int
        """

    def Rear(self):
        """
        :rtype: int
        """

    def isEmpty(self):
        """
        :rtype: bool
        """

    def isFull(self):
        """
        :rtype: bool
        """


    def printQueue(self):
        return self.queue

    
def main():
    myCircularQueue = MyCircularQueue(3)


if __name__ == '__main__':
    main()
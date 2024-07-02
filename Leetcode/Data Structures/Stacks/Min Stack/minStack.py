'''
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
    You must implement a solution with O(1) time complexity for each function.

    

    Example 1:

    Input
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

    Output
    [null,null,null,null,-3,null,0,-2]

    Explanation
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2
    

    Constraints:

    -231 <= val <= 231 - 1
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    At most 3 * 104 calls will be made to push, pop, top, and getMin.

'''

class MinStack(object):

    def __init__(self):
        #Creates an empty list as the stack
        self.stack = []
        #Stack to hold the sorted elements in the main stack
        self.min = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        #Adds the val to the end of the stack
        self.stack.append(val)
        #Adds the val to the min stack and sorts the elements in a reverse order
        self.min.append(val)
        self.min.sort(reverse=True)
        return 
        

    def pop(self):
        """
        :rtype: None
        """
        #Removes the last element from the stack
        popped_value = self.stack.pop()
        #Removes the popped value from the min stack
        self.min.remove(popped_value)
        #Deletes the popped_value from memory
        del popped_value 
        return 

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) != 0:
            return self.stack[-1]
        
        return None
        

    def getMin(self):
        """
        :rtype: int
        """
        #Returns the last element in the min stack
        return self.min[-1]
        

def main():
    minStack = MinStack()
    print(minStack.push(-2))
    print(minStack.push(0))
    print(minStack.push(-3))
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.min)
    print(minStack.getMin())

if __name__ == '__main__':
    main()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
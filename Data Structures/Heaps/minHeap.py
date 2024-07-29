'''

    Implement a heap data styructure that stores numeric 

    heapify(): Balances the heap

    insert(item): Adds an item to the heap

    find(item): Returns the node that contains the specified item

    findPartent(item): Returns the parent of the specified item

    findChildren(item): Returns the children of the specified item

    remove(item): Removes the specified item from the heap

    traverse(): Prints items in the heap from top to bottom

    heapsort(): Sorts the items in the heap

'''

class Heap:
    def __init__(self, capacity):
        #An array of zeros to store the elements in the heap
        self.storage = [0] * capacity
        #Sets the capacity of the heap to the capacity passed
        self.capacity = capacity
        #Sets the size of the heap to zero since it has no element yet
        self.size = 0

    #Returns the array when  the instantiated object is passed to the print function. Retruns the array as a string  
    def __str__(self):
        return str(self.storage)
    
    #Defines a method that helps to get the parent of the current node(index)
    def get_parent_index(self, index):
        return (index-1) // 2 

    #Defines a method that gets the left child of the current node(index)
    def get_left_index(self, index):
        return (2 * index) + 1
    
    #Defines a method that gets the right child of the current node(index)
    def get_right_index(self, index):
        return (2 * index) + 2
    
    #Defines a method that checks if a node(index) has a parent or not
    def has_parent(self, index):
        return self.get_parent_index(index) >= 0
    
    #Defines a method that checks if a node(index) has a left child
    def has_left_child(self, index):
        return self.get_left_index(index) < self.size
    
    #Defines a method that checks if a node(index) has a right child
    def has_right_child(self, index):
        return self.get_right_index(index) < self.size
    
    #Defines a method that returns the parent element of a specified node(index) in the heap Refine this method
    def get_parent(self, index):
        return self.storage[self.get_parent_index(index)]
    
    #Defines a method that returns the element at the left side of a specified node(index) Same
    def get_left(self, index):
        return self.storage[self.get_left_index(index)]
    
    #Defines a method that returns the element at the right side of the specified node(index) Same
    def get_right(self, index):
        return self.storage[self.get_right_index(index)]
    
    #Defines a method that checks if the heap is full or there is room to add elements to the heap
    def is_full(self):
        return self. size == self.capacity
    
    #Defines a method that swaps the data between the two specified indices. Will be called when an item is added or removed
    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

    #Defines a method that inserts an item to the heap
    #Iteration
    def insert(self, data):
        #Checks if the heap is full and throw an error
        if self.is_full():
            raise Exception('The Heap is Full')
        
        #Inserts the item at the current size position of the heap
        self.storage[self.size] = data

        #Increment the size by 1
        self.size += 1

        #Calls the heap_up method to heapify or to main the order of the heap
        self.heap_up()

    #Defines a method that heapify up the heap. Checks the order of the heap when an element is added to the heap 
    #Iteration
    def heap_up(self):
        index = self.size - 1

        #While loop to check if the node at that index has a parent and the parent is greater than the node at the current index
        while self.has_parent(index) and self.get_parent(index) > self.storage[index]:
            #Swaps the elements at the parent node and the current index
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    #Defines a method to insert an element to the heap using recursion
    #Recursion
    def insert_recursive(self, data):
        #Checks if the heap is full and throws an error if it is
        if self.is_full():
            raise Exception('The Heap is Full')
        
        #Adds the element to the heap
        self.storage[self.size] = data

        #Increments the size by 1
        self.size += 1

        #Calls the heap_up_recursive to maintain the order of the heap
        self.heap_up_recursive(self.size - 1)

    #Defines a method that heapify up the heap. Checks the order of the heap when an item is added to the heap
    #Recursive implementation
    def heap_up_recursive(self, size):
        #Checks if the current index has a parent and the parent is greater than the child node
        if self.has_parent(size) and self.get_parent(size) > self.storage[size]:
            #Swaps the elements at the parent node and the current node
            self.swap(self.get_parent_index(size), size)
            #Calls heap_up_ recursive function recursively until the base consition is met
            self.heap_up_recursive(self.get_parent_index(size))

    #Defines a method that removes and returns the min value (root) from the heap
    #Iteration
    def remove_min(self):
        #Checks if the heap is empty
        if self.size == 0:
            raise Exception('The Heap is Empty')
        
        #Puts the min value in the data variable
        data = self.storage[0]

        #Removes the last element and sets it to be the root element
        self.storage[0] = self.storage.pop()

        #Decrements the size of the heap by 1
        self.size -= 1

        #Calls the heap_down 
        self.heap_down()

        #Returns the min value
        return data

    #Defines a heap down method that maintains the order of the heap when the min value is removed
    #Iteration
    def heap_down(self):
        #Sets the current index to zero since we are starting from the root
        index = 0

        #Checks if the child node has a left child, a complete tree can only have a right child if it has a left child
        while self.has_left_child(index):
            #Sets the smaller child index to the left child index
            smaller_child_index = self.get_left_index(index)

            #Checks if the parent has a right node, if it does it checks whether the right element is less than the left
            if self.has_right_child(index) and self.get_right(index) < self.get_left(index):
                #if it is, it updates the smaller child index to the right index
                smaller_child_index = self.get_right_index(index)

            #Checks if child node is maller than the element at the parent node
            if self.storage[smaller_child_index] < self.storage[index]:
                #Swaps the elements if it does
                self.swap(index, smaller_child_index)

                #Sets the index to the index of the smaller child index to maintain the order in that node
                index = smaller_child_index

            else:
                break
    #Defines a method that removes and returns the min value (root) in the heap
    #Recursion
    def remove_min_recursive(self):
        #Checks if the size of the heap is 0
        if self.size == 0:
            raise Exception('The Heap is Empty')
        
        #Puts the min value in the data variable
        data = self.storage[0]

        #Removes the last element and sets it to be the root element
        self.storage[0] = self.storage.pop()

        #Decrements the size of the heap by 1
        self.size -= 1

        #Calls the heap_down 
        self.heap_down_recursive(0)

        #Returns the min value
        return data
    

    #Defines a heap down method that maintains the order of the heap when the min value is removed
    #Iteration
    def heap_down_recursive(self, index):
        #Sets the smallest value to the index of the root
        smallest = index

        #Checks if there is a left child and the left child is smaller than the parent node
        if self.has_left_child(smallest) and self.get_left(index) < self.storage[smallest]:
            #Sets the smallest to the index of the left child
            smallest = self.get_left_index(index)

        #Checks if the parent has a right child and the right child is smaller than the element at the smallest index
        if self.has_right_child(index) and self.get_right(index) < self.storage[smallest]:
            #Sets the smallest to the index of the right child
            smallest = self.get_right_index(index)

        #Checks if the smallest is not the same as the index
        if (smallest != index):
            #Swaps the elements at the smallest and index indices
            self.swap(smallest, index)

            #Calls the heap_down_recursive function recursively
            self.heap_down_recursive(smallest)


def main():
    heap = Heap(5)

    #print(heap)

    '''
    print(f'The parent index of the node at index 5 is {heap.get_parent_index(5)}')

    print(f'The left index of the node at 2 is {heap.get_left_index(2)}')

    print(f'The left index of the node at 2 is {heap.get_right_index(2)}')

    print(f'Is the node at index 2 having a parent {heap.has_parent(0)}')

    print(f'Is the heap full {heap.is_full()}')
    '''

    heap.insert(10)
    heap.insert(15)
    heap.insert(9)
    heap.insert(3)
    heap.insert(2)

    print(heap)

    print(f'The min value in the heap is {heap.remove_min()}')

    print(heap)

    '''
    heap.insert_recursive(10)
    heap.insert_recursive(15)
    heap.insert_recursive(9)
    heap.insert_recursive(3)
    heap.insert_recursive(2)

    print(heap)

    print(f'The min value in the heap is {heap.remove_min_recursive()}')

    print(heap)
    
    '''

if __name__ == '__main__':
    main()
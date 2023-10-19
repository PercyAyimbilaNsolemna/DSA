'''
    Implement a dynamic array in your chosen language with the following operations
    add(val)
        an element to the end of the array. 
        copy and double if necessary.
    get(i) - returns the element at index i, throw exception if out of bounds.
    set(i, val) - sets the value at index i to val. throw exception if out of bounds.
    size() - returns the size of the array
    capacity() - returns the capacity of the array
''' 

class Array:
    def __init__(self, *args):
        self._array = []
        for item in args:
            self._array.append(item)
    
    #Returns the array property whenm the array object is called by the ptint function   
    def __str__(self):
        return f'{self._array}'
    
    #Creates a getter for the array property using class decorators
    @property
    def array(self):
        return self._array
    
    #Creates a setter for the array property
    @array.setter
    def array(self, *args):
        for item in args:
            self._array.append(item)
            
    #Creates a var method that allows an item to be added to the end of the array
    #Time complexity O(1), space Complexity O(1)
    def add(self, var):
        self._array.append(var)
        
    #Creates a method that allows items to be added to the end of the array
    #Time complexity O(N) space Complexity O(1)
    def addMany(self, *vars):
        for value in vars:
            self._array.append(value)

    #Creates a method that returns the element at the specified index
    #Time complexity O(1), Space complexity O(1)
    def get(self, index):
        try:
            return self._array[index]
        except IndexError:
            return f'Index {index} out of range'
       #TODO: Add code to handle different types of errors tht can occur in the operation
       
    #Creates a method that sets the value at the specified index to a  different value
    #Time complexity O(1), Space complexity O(1)
    def set(self, index, value):
        try:
            self._array[index] = value
            return self._array
        except IndexError:
            return f'Index {index} is out of range'
        
    #Defines a method that returns the length of the array
    def size(self):
        return len(self._array)
    
    #Defines a method that adds an item to a specified index
    #TODO: Make it efficient, isn't efficient at the moment
    '''
    TO BE CONTINUED
    
    def put(self, index, value):
        try:
            for itemIndex in len(self._array):
                if itemIndex == index - 1:
                    self._array.append(value)
                elif itemIndex >= index:
                    self._array.append()
                    
        except IndexError:
            return f'Index {index} is out of range'
            
    '''
    
    #Should I understand the capacity method well, will implement it
    

def main():
    #Will contain code to test the array data structure implementattion
    array = Array(1, 2, 4)
    array.addMany(10, 20, 25)
    array.set(2, 30)
    print(array)
    print(array.size())
    
if __name__ == '__main__':
    main()
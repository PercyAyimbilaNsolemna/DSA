'''

    Hash Map Implementation
    Intro:
    Dictionary in python implements the hash map

    Hash map is the data structure dictionaries use under the hood

    Hash maps use a key to retrieve values stored in an array

    The hash function will be used to compute the index in the array where the value will be stored

    Values in a hash map are accessed using string index.

    The string index is converted to the corresponding array index which is then used to get the value in the array 

    computeHash(value): Computes and returns a key for  a given value. The ascii algorithm will be used to generate the key
                        The ascii algorithm will be used
                        The sum of all the chars in the key will be taken then a mod total number of items in the array
                        of the sum will be used as the index of that particular key

    insert(value): Adds the value to the hash map

     delete(item): Removes the item from the hash map basically the array

     search(item): Returns the item in the hash map

     getIndex(item): Returns the index of the item

     display(): Print out each item in the hash table 

'''

#Creates  the Hash Table class
class HashTable:
    #Defines an initialization method
    def __init__(self, max_size=100):
        #Sets the maximum size of the hash table to the max_size passed
        self.max_size = max_size

        #Creates an array of the same size as the maximum size specified
        self.array = [None] * self.max_size

    #Defines the hash function. This will be used to calculate the index of the key passed to the hash function
    def hash(self, key):
        index = 0

        #Loops through all the chars in the key to calculate the ascii sum
        for char in key:
            index += ord(char)

        #Takes mod of the max_size of the ascii sum and returns it
        return index % self.max_size
    

    #Defines  a method that adds an item to the hash table
    def insert(self, key, value):
        #Calls the hash method to get the index of the key
        index = self.hash(key)

        #Inserts the value to the index returned from the hash method
        self.array[index] = value

    #Defines a method that allows insertion using curly brackets 
    def __setitem__(self, key, value):
        #Calls the hash method to get the index of the key
        index = self.hash(key)

        #Inserts the value to the index returned from the hash method
        self.array[index] = value

    #Defines a method that returns the value in a specified key
    def get(self, key):
        #Calls the hash method to get the index of the key
        index = self.hash(key)

        #Returns the value at the specified index returned from the hash function
        return self.array[index]

    #Defines a method that allows getting items using curly brackets
    def __getitem__(self, key):
        #Calls the hash method to get the index of the key
        index = self.hash(key)

        #Returns the value at the specified index returned from the hash function
        return self.array[index]

    
    #Defines a method that deletes a value by key
    def delete(self, key):
        #Calls the hash method to the index of the specified key
        index = self.hash(key)

        #Sets the value of the index of the key to None
        self.array[index] = None

    #Defines a method that allows dleting an item using curly brackets
    def __delitem__(self, key):
        #Calls the hash method to the index of the specified key
        index = self.hash(key)

        #Sets the value of the index of the key to None
        self.array[index] = None

    #Defines a method that returns the index of the key calculed from the hash used to insert the value into the array
    def getIndex(self, key):
        #Calls the hash method to return the index of the key
        return self.hash(key)

    #Defines a method that prints all the items in the hash table 
    def display(self):
        for value in self.array:
            if value is not None:
                print(value)

def main():
    hashTable = HashTable()

    hashTable.insert('march 6', 'Cat')

    print(hashTable.get('march 6'))

    print(hashTable.getIndex('march 6'))

    hashTable['march 10'] = 'Enjoyment!'

    print(hashTable['march 10'])

    hashTable['march 11'] = 'Money Finish'

    del hashTable['march 11']
 
    hashTable.display()

if __name__ == '__main__':
    main()
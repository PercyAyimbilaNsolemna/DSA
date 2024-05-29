'''
    Implementation of the matrix data structure

    With the below method for a matrix opeartion

    zeros: This creates a matrix with zeros based on the shape specified
    insert (item, i, j): Inserts an item at the given position
    traverse(item): Print out every cell value of a matrix
    search(item): Return true or false if an item can be found in a matrix
    getIndex(item): Returns the idex i and j of an item in a matrix
    reverseRow(rowIndex): Reverse elements of a specific row
    reverseColumn(columnIndex): Reverse elements of a specific column
    sort(item): Remove node containg a specified item
    diagonalSum(): Returns the sum of cells along the matrix primary diagonal
    display(): Print out every cell data in a matrix

'''

class Matrix:
    #When initializing the matrix the dimensions of the matrix can be passed in as an argumnet
    #Or it can be passed in as a string
    #Mimicking the numpy implementation of matrix
    def __init__(self, dimensions=None):
        self.matrix = []
        if type(dimensions) == str:
            #Removes any space after the semicolon before splitting the text into dimensions
            splitted_text = dimensions.replace('; ', ';').split(';')
            #Checks if there is a decimal in any of the entries. Help type cast all the entries to float
            find_decimal = '.' in dimensions
            if len(splitted_text) == 1 and splitted_text[0] == '':
                print('Exiting here!')
                print(self.matrix)
                return         
            for row_in_text in splitted_text:
                row_string = row_in_text.split(' ')
                for index in range(len(row_string)):
                    #print('The code has entered here!')
                    #Add a condition to remove any space that will be included in the matrix
                    if find_decimal:
                        try:
                            row_string[index] = float(row_string[index])
                        except:
                            print(f'The number {row_string[index]} can not be converted to a decimal')
                    else:
                        try:
                            row_string[index] = int(row_string[index])
                        except:
                            print((f'The number {row_string[index]} cannot be converted to an integer'))

                self.matrix.append(row_string)
            print(self.matrix)
            return
        elif dimensions == None:
            self.matrix = []
            return
        else:
            self.matrix = dimensions
            print(self.matrix)
            return

    #Creates an zero matrix based on the number of rows and columns specified
    def zeros(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[0 for x in range(columns)] for y in range(rows)]
        print(self.matrix)

    #Method that inserts an item at a given position
    def insert(self, item, i, j):
        #Use exceptions to check if the index specified is in the matrix
        try:
            item_to_change = self.matrix[i][j]
        except IndexError:
            print(f'The index {i}th row and {j}th column is not in the matrix: \n{self.matrix}')
            return

        #Converts the item to be inserted to the correct data type
        data_type = type(item_to_change)

        try:
            casted_item = data_type(item)
        except ValueError:
            print(f'The item {item} cannot be type casted')
            return 
        
        self.matrix[i][j] = casted_item

        #Deletes the data_type and item_to_change variables to save memory
        del item_to_change, data_type

        print(f'The new matrix is: \n{self.matrix}')

    #Method that prints out every cell value of a matrix
    def traverse(self):
        for row_index in range(0, len(self.matrix)):
            for column_index in range(0, len(self.matrix[row_index])):
                print(f'{self.matrix[row_index][column_index]}')

    #Method that returns True if an element can be found in the matrix and False otherwise
    def search(self, item):
        for row_index in range(0, len(self.matrix)):
            for column_index in range(0, len(self.matrix[row_index])):
                if self.matrix[row_index][column_index] == item:
                    return True
                
        return False

def main():
    matrix = Matrix([[1, 2, 3], [3, 4, 5], [6, 7, 8]])

    matrix1 = Matrix('1 2 3; 4 5 6')

    matrix.zeros(2, 3)

    matrix.insert(2, 1, 2)

    matrix.traverse()

    print(matrix.search(3))


if __name__ == '__main__':
    main()
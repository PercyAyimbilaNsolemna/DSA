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
        return self.matrix

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
    
    #Method that returns the index i and j of an element if it is in the linked list and None otherwise
    def getIndex(self, item):
        for row_index in range(0, len(self.matrix)):
            for column_index in range(0, len(self.matrix[row_index])):
                if self.matrix[row_index][column_index] == item:
                    return f'The ith and jth indexes are {row_index}, {column_index}'       
        return f'The item {item} was NOT found in the matrix'
    
    #Method that reverses elements of a specific row
    def reverseRow(self, rowIndex):
        #Stores the min value of the elements in the row
        min = 0
        try:
            #Stores the length of the row
            max = len(self.matrix[rowIndex]) - 1
        except IndexError:
            return f'The row index {rowIndex} is OUT OF RANGE'

        #Loops through the specified row
        for _ in range(0, len(self.matrix[rowIndex])):
            #Reverses the elements in place
            self.matrix[rowIndex][min], self.matrix[rowIndex][max] = self.matrix[rowIndex][max], self.matrix[rowIndex][min]
            #Increments the min value
            min += 1
            #Decrements the max value
            max -= 1
            #Checks if all the elements have been reversed and break out of the loop
            if min == max or min > max:
                return self.matrix
            
    #Methos that reverses elements in a specified column
    def reverseColumn(self, columnIndex):
        #Stores the min value 
        min = 0
        #Stores the max value of the column
        max = len(self.matrix) - 1

        try:
            for _ in range(0, len(self.matrix)):
                #Reveres the elements in place
                self.matrix[min][columnIndex], self.matrix[max][columnIndex] = self.matrix[max][columnIndex], self.matrix[min][columnIndex]
                #Increment min
                min += 1
                #Decrements max
                max -= 1
                if min == max or min > max:
                    return self.matrix       
        except IndexError:
            return f'The column index {columnIndex} is OUT RANGE'
        
    #Method that removes a specified item. The specifics of this method is not clear. Will work on it when resolved
    def sort(self, item):
        ...

    #Method that returns the sum of cells along the matrix primary diagonal
    def diagonalSum(self):
        sum = 0

        for row_index in range(0, len(self.matrix)):
            for column_index in range(0, len(self.matrix[row_index])):
                if row_index == column_index:
                    sum += self.matrix[row_index][column_index]
        
        return f'The sum of the cells along the main diagonal is {sum}'
    
    #Method that prints all the cells in the matrix
    def display(self):
        for row_index in range(0, len(self.matrix)):
            for column_index in range(0, len(self.matrix[row_index])):
                print(f'{self.matrix[row_index][column_index]}')

    ##Method that transposes the matrix
    def transpose(self):
        #Gets the inintial number of rows in the matrix
        rowsInintial = len(self.matrix)
        #Error checking for when the matrix is empty
        if rowsInintial == 0:
            return 'The matrix is empty'
        
        #Gets the initial number of columns in the matrix
        columnsInitial = len(self.matrix[0])

        #Saves the matrix to be transposed in a variable called original matrix
        original_matrix = self.matrix

        #Calls the zeros method to create zeros matrix of the transposed matrix 
        transpoed_matrix = self.zeros(columnsInitial, rowsInintial)
        
        #Loops through the matrix to be transposed and inserts the elements in the zero created transposed matrix
        for row_index in range(0, len(original_matrix)):
            for column_index in range(0, len(original_matrix[row_index])):
                #Swaps the rows with the columns 
                transpoed_matrix[column_index][row_index] = original_matrix[row_index][column_index]
        #Deletes the transposed_matrix, original matrix, rows initial and column initial variables created to free up memory
        del transpoed_matrix, original_matrix, rowsInintial, columnsInitial

        #Return the transposed matrix
        return self.matrix
    
def main():
    matrix = Matrix([[1, 2, 3], [3, 4, 5], [6, 7, 8]])

    matrix1 = Matrix('1 2 3; 4 5 6')

    matrix.zeros(2, 3)

    matrix.insert(2, 1, 2)

    matrix_new = Matrix()

    print(matrix_new.transpose())

    #matrix.traverse()

    #print(matrix.search(2))

    #print(matrix.getIndex(2))

    #print(matrix1.reverseRow(0))
    #print(matrix1.reverseRow(5))
    #print(matrix1.reverseColumn(0))
    #print(matrix1.diagonalSum())
    
    #matrix1.display()


if __name__ == '__main__':
    main()
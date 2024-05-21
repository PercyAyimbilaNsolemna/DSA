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
            splitted_text = dimensions.split(';')
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

    def zeros(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[0 for x in range(columns)] for y in range(rows)]
        print(self.matrix)



def main():
    matrix = Matrix([[1, 2, 3], [3, 4, 5], [6, 7, 8]])

    matrix.zeros(2, 3)


if __name__ == '__main__':
    main()
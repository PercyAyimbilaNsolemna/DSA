'''
    Implementation of the matrix data structure

    With the below method for a matrix opeartion

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
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[0 for x in range(columns)] for y in range(rows)]
        print(self.matrix)


def main():
    matrix = Matrix(4, 3)


if __name__ == '__main__':
    main()
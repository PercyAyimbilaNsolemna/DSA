'''
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109

'''

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]

       """

        #Creates a zero matrix of the same shape as the transposed matrix
        transposed_matrix = [[0 for x in range(len(matrix))] for y in range(len(matrix[0]))]

        transposed_matrix_1 = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        print(transposed_matrix_1)

        #Loops through the original matrix and reverse the rows and ciolumns
        for row_index in range(0, len(matrix)):
            for column_index in range(0, len(matrix[row_index])):
                transposed_matrix[column_index][row_index] = matrix[row_index][column_index]

        #Deletes the rows initial and the column initial variables created in memory
        #del rowsInitial, columnsInitial

        #Returns the transposed matrix
        return transposed_matrix
        
def main():
    solution = Solution()

    print(solution.transpose([[1,2,3],[4,5,6]]))


if __name__ == '__main__':
    main()
'''
    Given an array arr of integers, check if there exist two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]
    
    Example 1
    Input: arr = [10,2,5,3]
    Output: true
    Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
    
    Example 2
    Input: arr = [3,1,7,11]
    Output: false
    Explanation: There is no i and j that satisfy the conditions.
    
    Constraints
    2 <= arr.length <= 500
    -103 <= arr[i] <= 103
    
    Algorithm
    Multiply each of the elements in the arr by 2
    check if any of the numbers in the new is in the old array
'''

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for number in arr:
            twiceNumber = 2 * number
            if number == 0:
                if arr.count(0) >= 2:
                    return True
            elif twiceNumber in arr:
                return True
        return False
        
def main():
    solution = Solution()
    print(solution.checkIfExist([-2,0,10,-19,4,6,-8,0]))
    #[10,2,5,3]
    #[3,1,7,11]
    
if __name__ == '__main__':
    main()
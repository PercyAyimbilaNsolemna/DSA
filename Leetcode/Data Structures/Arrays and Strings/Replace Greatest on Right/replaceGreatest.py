'''
    Given an array arr, replace every element in that array with the greatest element among the elements to its right, 
    and replace the last element with -1.

    After doing so, return the array.

    Example 1
    Input: arr = [17,18,5,4,6,1]
    Output: [18,6,6,6,1,-1]
    Explanation: 
    - index 0 --> the greatest element to the right of index 0 is index 1 (18).
    - index 1 --> the greatest element to the right of index 1 is index 4 (6).
    - index 2 --> the greatest element to the right of index 2 is index 4 (6).
    - index 3 --> the greatest element to the right of index 3 is index 4 (6).
    - index 4 --> the greatest element to the right of index 4 is index 5 (1).
    - index 5 --> there are no elements to the right of index 5, so we put -1.

    Example 2
    Input: arr = [400]
    Output: [-1]
    Explanation: There are no elements to the right of index 0.

    Constraints
    1 <= arr.length <= 104
    1 <= arr[i] <= 105

    Algorithm 
    Loop through the array given 
    Get the value of the element at index 0
    Compare with all the elements on the right hand side, change the element withe the greatest element on the right
    Repeat the above steps until the last but one index is reached
    Replace the last element with -1
'''

class Solution(object):
    def replaceGreatestElement(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        #TODO: Edit the code from O(n²)
        for index in range(len(arr)-1):
            max_number = max(arr[index+1:])
            arr[index] = max_number
        
        arr[len(arr)-1] = -1
        return arr
    
    def optimize_array(self, arr):
        n = len(arr)
        
        # Initialize the maximum value to -1
        max_value = -1
        
        # Iterate in reverse order
        for i in range(n - 1, -1, -1):
            current_element = arr[i]
            
            # Update the current element with the maximum value encountered so far
            arr[i] = max_value
            
            # Update the maximum value if the current element is greater
            max_value = max(max_value, current_element)
        
        return arr


def main():
    solution = Solution()

    #print(solution.replaceGreatestElement([17,18,5,4,6,1]))

    print(solution.optimize_array([17,18,5,4,6,1]))

if __name__ == '__main__':
    main()
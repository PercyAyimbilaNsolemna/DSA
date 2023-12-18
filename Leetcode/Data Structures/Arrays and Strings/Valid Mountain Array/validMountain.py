'''
    Given an array of integers arr, return true if and only if it is a valid mountain array.

    Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

    Example 1
    Input: arr = [2,1]
    Output: false

    Example 2
    Input: arr = [3,5,5]
    Output: false

    Example 3
    Input: arr = [0,3,2,1]
    Output: true

    Algorithm
    Traverse the array from start, compare if the leading number is greater than the previous number
    Traverse to a point where the index is smaller than the previous number
    Traverse from that index to the last element comparing that all the leading elements are smaller than the 
    previous element
    Else return false
'''

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        if len(arr) < 3:
            return False
        
        index = 0

        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                index = i
                break
            elif arr[i-1] == arr[i]:
                return False
            
        if index == len(arr):
            return False
 
        for j in range(index+1, len(arr)):
            if arr[j-1] < arr[j] or arr[j-1] == arr[j] or index == 1:
                return False
            
        return True


def main():
    solution = Solution()
    print(solution.validMountainArray([9,8,7,6,5,4,3,2,1,0]))


if __name__ == '__main__':
    main()